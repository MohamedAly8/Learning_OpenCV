#Camera and VideoCapture
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    #ret: True/False state of video
    #frame: numpy array of frame
    ret, frame = cap.read()

    #get width property of video capture
    width = int(cap.get(3))
    #get height property of video VideoCapture
    height = int(cap.get(4))

    #Draw a line (Top left is 0,0 in image)  Arguments (source image, start_point, end_point, color in BRG, Width of line)
    img = cv2.line(frame, (0,0), (width, height), (255,0,0) , 10)

    #Draws another line from bottom left to top right 
    img = cv2.line(img, (0,height), (width, 0), (255,0,0) , 10)

    #Drawing rectangle arguments: (source image, top left point, bottom right point, color BGR, thickness)
    img = cv2.rectangle(img, (width//4, height//4), (int(width//(4/3)), int(height//(4/3))), (0,250,0), 2)

    #Drawing circle argyments: (source imgage, center, radius, color BGR, thickness)
    img = cv2.circle(img, (width//2, height//2), (width//4), (0,0,250), 2)

    #Drawing text args: (source image, text, bottom left corner, font, font scale, color, thickness, line type)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Hello there", (50, height-50), font, 4, (250,250,250),5,cv2.LINE_AA)

    #Shows the frame image, which contains 4 videos now
    cv2.imshow('frame',frame)


    #Stops the while loop, checks every 1 millisecond
    if cv2.waitKey(1) == ord('q'):
        break


#Releases camera resource so something else can use it
cap.release()
cv2.destroyAllWindows()
