import cv2 as cv

img = cv.imread('.Photos/image.jpg')
cv.imshow('Ex', img)

# chinh kich thuoc frame cho img, video, live video
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
capture = cv.VideoCapture('.Videos/video.mp4')

# chinh sua kich thuoc cho live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()
    
    frame_resize = rescaleFrame(frame)
    cv.imshow('Video', frame_resize)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()

#