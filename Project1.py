import cv2


'''How to read an image, second parameter
 -1 : loads a color image
 0  : loads image in grayscale
 1  : loads image unchanged
'''
#Read image
img = cv2.imread('assets/logo.png', )

#Resizes image 
# When using fx, fy, set image size to (0,0)
img = cv2.resize(img, (0,0), fx=0.5, fy = 0.5)


#Rotate image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)


#Save image, writes img into new file
cv2.imwrite('new_img.png', img)

#Display image
cv2.imshow('Image', img)


#Wait infinite amount of time, destroys all windows if key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

