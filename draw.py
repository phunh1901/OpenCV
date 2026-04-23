import cv2 as cv
import numpy as np

# img = cv.imread('.Photos/image.jpg')
# cv.imshow('Photo', img)

#color BGR
blank = np.zeros((500, 500, 3), dtype='uint8')
blank[:] = 0,0,0

# Draw Rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# Draw Line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
cv.imshow("Line", blank)

# Write text
cv.putText(blank, 'Hi', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)


#