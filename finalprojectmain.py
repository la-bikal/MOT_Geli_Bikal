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

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt_tree.xml")
    # all detected face were correct

    face_cascade2 = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


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
        # fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)

        # Detect faces
        detected_facesfirst = face_cascade.detectMultiScale(gray)
        defaultface=[]

        for (column, row, width, height) in detected_facesfirst:
            defaultface=cv2.resize(gray[row:row + height, column:column + width], dim, interpolation=cv2.INTER_AREA)
            ret, defaultface_thresh = cv2.threshold(defaultface,127, 255,0)
            defaultface_contours, hierarchy = cv2.findContours(defaultface_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            defaucont=defaultface_contours[0]
        print("====")
        print(defaucont)
        print("default contours printed")
        cv2.imshow("default face",defaultface)
        print(defaultface.shape)






        # draw a rectangle on the detected faces
        detectedfacelist=[]
        positionlist=[]
        resizedlist = []


        cnt = 0
        detected_faces = face_cascade2.detectMultiScale(gray)
        for (column, row, width, height) in detected_faces:

            detectedfacelist.append([cnt,column,row,width,height,gray[row:row+height,column:column+width]])
            resizedlist.append([cnt,column,row,width,height,cv2.resize(gray[row:row+height,column:column+width], dim, interpolation=cv2.INTER_AREA)])
            # cv2.rectangle(frame, (column,row), (column + 10, row + 10), (0, 255, 0), 2)
            # ret, thresh = cv2.threshold(gray[row:row+height,column:column+width], 127, 255, 0)
            cv2.rectangle(frame, (column, row), (column +width, row + height), (0, 255, 0), 2)
            positionlist.append([cnt, column,row])
            cnt = cnt + 1

            center_coordinates = (column, row)
            radius = 30
            color = (0, 0, 255)
            thickness = -1
            frame = cv2.circle(frame, center_coordinates, radius, color, thickness)

        print(detectedfacelist)
        # for m in range(len(detectedfacelist)):
        #     cv2.imshow("number"+str(m),detectedfacelist[m][1])
        #     print("xx")
        for m in range(len(resizedlist)):
            cv2.imshow("number" + str(m), resizedlist[m][5])
            # print("xx")

        for k in range(len(resizedlist)):
            if k ==0:
                cur_column = resizedlist[k][1]
                cur_row=resizedlist[k][2]
                cur_width=resizedlist[k][3]
                cur_height=resizedlist[k][4]

                ret, cur_thresh = cv2.threshold(gray[cur_row:cur_row + cur_height, cur_column:cur_column + cur_width], 127, 255, 0)
                print("=================================")
                print(cur_thresh.shape)
                print("=================================")

                cur_thresh=cv2.resize(cur_thresh, dim, interpolation=cv2.INTER_AREA)
                cur_contours, hierarchy = cv2.findContours(cur_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                # cv2.imshow("inside range",gray[cur_row:cur_row + cur_height, cur_column:cur_column + cur_width])
                if len(cur_contours)==0:
                    print("warning")

                # oval = cv2.matchShapes(cur_contours[0], defaucont, cv2.CONTOURS_MATCH_I2, 0.0)
                # print(oval)
                print("matchscore printed")





























            # for i in range(len(detected_faces)):
            #     cv2.imshow("area of interest at " + str(i), gray[row:row + height, column:column + width])

            #
            #
            # faces=len(detected_faces)
            # cv2.rectangle(frame, (column, row), (column + width, row + height), (0, 255, 0), 2)
            # ret, thresh = cv2.threshold(gray[row:row+height,column:column+width], 127, 255, 0)
            # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cv2.imshow("area of interest",gray[row:row+height,column:column+width])
            #
            # if len(contours)==0:
            #     pass
            # else:
            #     counterlabel=0
            #     print("start printing contours")
            #     print(contours)
            #     print("len of contours="+str(len(contours)))
            #     for i in range(len(contours)):
            #         currM = cv2.moments(contours[i])
            #         if currM['m00'] != 0:
            #             counterlabel = counterlabel + 1
            #             cx = int(currM['m10'] / currM['m00'])
            #             cy = int(currM['m01'] / currM['m00'])
            #             print(counterlabel,cx,cy)
            #             print("i,cx,cy printed")
            #             cv2.rectangle(frame, (cx, cy), (cx+10, cy + 10), (0, 255, 0), 2)
                        #         facelist.append([counterlabel, column, column + width, row, row + height, contours[0]])


                # for contour in contours:
                #     M = cv2.moments(contour)
                #     if M['m00'] != 0:
                #         counterlabel = counterlabel + 1
                #         cx = int(M['m10'] / M['m00'])
                #         cy = int(M['m01'] / M['m00'])
                #         print(counterlabel,cx,cy)
                #         print("i,cx,cy printed")
                #         facelist.append([counterlabel, column, column + width, row, row + height, contours[0]])
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (25, 0, 100)
        thickness = 2
        frame = cv2.putText(frame, 'Number of objects:'+str(len(detected_faces)), org, font,
                            fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow(winname,frame)
        cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
