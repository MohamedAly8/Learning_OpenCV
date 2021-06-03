import cv2
import random


# Read img
img = cv2.imread('assets/logo.png', -1)

# [0,0,0] blue green red
# [255,0,0] -> blue

#img is a numpy array of pixel BGR (Blue Green Red)
# print(img.shape)


#show first row
#print(img[0])

#show row 257
# print(img[100][100])

# Changes the first 100 rows of pixels of an image to random color pixels
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randrange(255),random.randrange(255),random.randrange(255)]

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Copy part of image by copying part of array
tag = img[75:100, 46:90]

#Paste the copied tag back in another part of array
img[0:25,0:44] = tag

#Show the image after copying
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()