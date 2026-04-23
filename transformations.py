import cv2 as cv
import numpy as np

img = cv.imread('.Photos/image.jpg')
cv.imshow('Dog', img)
print(img.shape)

# Translation
def translate(img, x, y):
    # MT 2x3: So 1 giu nguyen ty le img
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# x -> right
# y -> down
# opposite

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rote(img, angle, rotPoint=None):
    height, width = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    # xoay theo goc angle(độ)
    # angle > 0 -> nguoc chieu kim dong ho
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 2.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

# Khi xoay thêm những phần đen vào vùng trống
rotated = rote(img, 45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
# 0 -> Flip theo x
# 1 -> Flip theo y
# -1 -> Flip theo x + y
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# Cropping
cropped = img[0:100][0:100]
cv.imshow('Cropped', cropped)

cv.waitKey(0)