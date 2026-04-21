import cv2 as cv
import numpy as np

# img = cv.imread('.Photos/image.png')
# cv.imshow('Photo', img)

#color BGR
blank = np.zeros((500, 500, 3), dtype='uint8')
blank[:] = 0,0,0

cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
cv.imshow('Blank', blank)

cv.waitKey(0)