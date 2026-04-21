import cv2 as cv

img = cv.imread('.Photos/image.jpg')
cv.imshow('Dog', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur: Làm mờ
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascace: lấy viền
canny = cv.Canny(blur , 125, 127)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resize', resized)

# Cropping
cropped = img[0:250, 100:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)