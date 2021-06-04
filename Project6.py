import cv2
import numpy as np


img = cv2.imread('chessboard.png')

#Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Runs Shi-Tomasi Corner Detection Algorithm args: (src image, max num of corners, quality 0 to 1, minimum euclidean distance between corners delta x^2 + delta y^2 = r^2 )
corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)

#Converts floats in np array to int
corners = np.int0(corners)

for corner in corners:
    #Flattens an aray, removes interior arrays [[[0],[1],[2]]]] -> [0,1,2]
    x, y = corner.ravel()
    #Draws circles at corners
    cv2.circle(img,(x,y),10,(0,0,255),2)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        # args: low , high, size
        color = tuple(map(lambda x: int(x), np.random.randint(0,255,size=3)))
        cv2.line(img,corner1,corner2, color, 1)


cv2.imshow('Frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
