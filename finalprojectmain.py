import numpy as np
import cv2
import sys


def main():
    # resize dimensions can be changed here
    imagewidth = 300
    imageheight = 400
    dim = (imagewidth, imageheight)

    # The default capture device is the default video source.
    cap = None
    cap = cv2.VideoCapture(r"C:\Users\lee\Desktop\imagesource\finalproject\walking\walking\walking2.mp4")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


    # Create a window
    winname = "Faces"
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    hasframe = True
    facedict=dict()
    facelist=[]

    while(hasframe):
        # Capture frame-by-frame
        hasframe, frame = cap.read()

        # Convert the frame to grayscale

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        # Detect faces
        detectedfacelist=[]
        positionlist=[]
        resizedlist = []


        detected_faces = face_cascade.detectMultiScale(gray)
        count=0
        for (column, row, width, height) in detected_faces:
            count+=1
            cv2.rectangle(frame, (column, row), (column +width, row + height), (0, 255, 0), 2)



        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (25, 0, 100)
        thickness = 2
        frame = cv2.putText(frame, 'Number of objects:'+str(count), org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow(winname,frame)
        cv2.waitKey(30)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


