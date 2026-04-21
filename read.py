import cv2 as cv

#img = cv.imread('.Photos/image.p'jpg

# cv.imshow("Ex", img)

capture = cv.VideoCapture('.Videos/video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()


