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

    # Creating empty numpty array as image canvas
    image = np.zeros(frame.shape, np.uint8)

    #make quarter of video size frame
    smaller_frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)

    #top left
    image[:height//2, :width//2] = smaller_frame

    #bottom left
    image[height//2:, :width//2] = cv2.flip(smaller_frame, 1)

    #top right
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)

    #bottom right
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)

    #Shows the frame image, which contains 4 videos now
    cv2.imshow('frame',image)


    #Stops the while loop, checks every 1 millisecond
    if cv2.waitKey(1) == ord('q'):
        break


#Releases camera resource so something else can use it
cap.release()
cv2.destroyAllWindows()
