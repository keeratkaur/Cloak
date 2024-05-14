import cv2 
import numpy as np

cap=cv2.VideoCapture(0)
background=cv2.imread('./image.jpg')

while cap.isOpened():
    #capturing teh frame in live mode
    ret, current_frame=cap.read()
    if ret:
        #convert rgb to hsv
        hsv_frame=cv2.cvtColor(current_frame,cv2.COLOR_BGR2HSV)

        #set range for color detection (brown color)
        #lower brown
        l_brown=np.array([0, 50, 20]) 
        u_brown=np.array([30, 255, 150]) 
        mask1=cv2.inRange(hsv_frame,l_brown,u_brown)

        #upper brown
        l_brown= np.array([150, 50, 20]) 
        u_brown=np.array([179, 255, 150])
        mask2=cv2.inRange(hsv_frame,l_brown,u_brown)

        #generate final brown mask
        brown_mask= mask1+mask2

        brown_mask=cv2.morphologyEx(brown_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=10)
        brown_mask = cv2.morphologyEx(brown_mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
        #combing brown portion with bg image
        part1=cv2.bitwise_and(background,background, mask=brown_mask)

        #detect non brown things
        brown_free=cv2.bitwise_not(brown_mask)

        #if brown cloak is not there: show origial bg
        part2=cv2.bitwise_and(current_frame,current_frame, mask=brown_free)

        #final output

        cv2.imshow("cloak", part1+part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()