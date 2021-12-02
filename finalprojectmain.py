
import numpy as np
import cv2
import sys

def main():

    # The default capture device is the default video source.
    cap = None
    # if len(sys.argv) > 1:
    #     source = sys.argv[1]
    #     try:
    #         cap = cv2.VideoCapture(source)
    #     except:
    #         sys.exit("Invalid video file.")
    # else:
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(r"C:\Users\lee\Desktop\imagesource\finalproject\walking\walking\walking2.mp4")

    # Load in the frontal face classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # backpacks and shirts are classified as face



    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt_tree.xml")
    # all detected frontal face were correct, main issue: missing detection



    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
    # worse than the default, unstable

    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    # # - -
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml")
    # pretty bad

    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
    # bad


    # haarcascade_frontalface_alt2.xml
    # haarcascade_lowerbody.xml
    # haarcascade_frontalface_alt_tree.xml
    # haarcascade_profileface.xml
    # haarcascade_frontalface_default.xml
    # haarcascade_fullbody.xml
    # haarcascade_frontalface_alt.xml
    # haarcascade_upperbody.xml

    # Create a window
    winname = "Faces"
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)

    hasframe = True
    while(hasframe):
        # Capture frame-by-frame
        hasframe, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        detected_faces = face_cascade.detectMultiScale(gray)

        # draw a rectangle on the detected faces
        for (column, row, width, height) in detected_faces:
            print("detection")
            print(len(detected_faces))

            print(detected_faces)
            print("detection shown")
            cv2.rectangle(frame,(column, row),(column + width, row + height),(0, 255, 0),2)


        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (25, 0, 100)
        thickness = 2
        frame = cv2.putText(frame, 'Number of objects:'+str(len(detected_faces)), org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow(winname,frame)
        cv2.waitKey(1)
        # if cv2.waitKey(1) == ord('q'):
        #     break

    # When everything's done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
