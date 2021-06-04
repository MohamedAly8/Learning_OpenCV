import cv2
import numpy as np

#arg 0 -> grayscale
img = cv2.imread('assets/soccer_practice.png', 0)
template = cv2.imread('assets/ball.png', 0)


#no 3rd arg since it is grayscale, no color
h, w = template.shape

# Different ways to perform template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    #result : (W-w + 1, H-h + 1) W/H: width/heigh of base img 
    result = cv2.matchTemplate(img2, template, method)

    # Resuts min val, max val, min loc and max loc of result array
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #this is where min is best 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    btm_right = (location[0]+w, location[1]+h)
    cv2.rectangle(img2, location, btm_right, 255, 2)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


# Assume image is 4x4
# Assume template is 2x2

#W = 4
#w = 2
#H = 4
#h = 2
# result = (4-2 + 1 , 4-2 + 1) = (3,3)

#Base Image
#[[255, 255, 255, 255],
# [255, 255, 255, 255],
# [255, 255, 255, 255],
# [255, 255, 255, 255]]

#Template
# [[255, 255],
#  [255, 255]]

#Slide Template over Base Image 

#Result: Find 1, since that is where match occurs
# [[0, 0, 0],
#  [0, 1, 0],
#  [0, 0, 0]]