import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#hsv : hue saturation value

while True:
    ret, frame = cap.read()
    width, height = int(cap.get(3)), int(cap.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Need to pick lower bound and upper bound of colors we are trying to extract
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    #part of image/frame with only blue pixels existing. Pixels in range of lower-upper blue
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    # 1 1 = 1
    # 0 1 = 0
    # 1 0 = 0
    # 0 0 = 0
    #bitwise and uses mask to determine wether or not to keep each pixel. 
    #Comparing bits from mask to bits in image -> If 1 1 keep pixel, else make pixel black
    result = cv2.bitwise_and(frame,frame,mask=mask)

    

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

