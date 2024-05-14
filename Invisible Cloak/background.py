import cv2
#creating a video capture object
cap=cv2.VideoCapture(0) # passing 0 because webcam will capture the video

#Getting bg image
while cap.isOpened():
    ret,background = cap.read() #read from webcam
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord('q'):
            #save bg image
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()