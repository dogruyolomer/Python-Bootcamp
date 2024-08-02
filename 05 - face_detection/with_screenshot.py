import numpy as np
import cv2
import time


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )  # load the Haar Cascade model 

def TakeSnapshotAndSave():
    cap = cv2.VideoCapture(0) # access to the webcam
    
    num =0
    while (True):
        ret, frame = cap.read() # capture frame by frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) # detect face 

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # write on the live stream video
        # x = 0
        # y = 20
        # text_color = (0,255,0)
        # cv2.putText(frame, "Press 't' for screenshot", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=2)

        # Display the resulting frame
        cv2.imshow("Press 'q'for quit or 's' for screenshot ",frame)

        if cv2.waitKey(1) & 0xFF == ord("q"): # q for quit
            break

        elif cv2.waitKey(1) & 0xFF == ord("s") : # s for take a screenshot and save
            cv2.imwrite('opencv'+str(num+1)+'.jpg',frame) # write the captured image with this name
            num = num+1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    TakeSnapshotAndSave()