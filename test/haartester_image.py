#opens up a webcam feed so you can then test your classifer in real time
#using detectMultiScale
import numpy
import cv2

def detect(img):
    cascade = cv2.CascadeClassifier("cascade20.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (50,50))

    if len(rects) == 0:
	print("WHERE THE FUCK IS MY GEORGY")
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    #cv2.imwrite('one.jpg', img);


img = cv2.imread("scaling24.jpg")
rects, img = detect(img)
box(rects, img)
cv2.imwrite("fred_frame.jpg", img)
