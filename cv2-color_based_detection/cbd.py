
import cv2 as cv
import numpy as np
import cv2



def rescal_frame(frame, scale_factor=0.5):
    """"
    a function to rescale a frame by a giving factor

    """
    h = int(frame.shape[0] * scale_factor)
    w = int(frame.shape[1] * scale_factor)
    dim = (w, h)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def temp(a):
    pass

""" Creating GUI for HSV values manipulation """

cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars',640,240)

cv.createTrackbar('H Min','TrackBars',0,179,temp)
cv.createTrackbar('H Max','TrackBars',179,179,temp)

cv.createTrackbar('S Min','TrackBars',0,255,temp)
cv.createTrackbar('S Max','TrackBars',40,255,temp)

cv.createTrackbar('V Min','TrackBars',156,255,temp)
cv.createTrackbar('V Max','TrackBars',255,255,temp)
kernel = np.ones((5,5),np.uint8)

while True:

    img = cv.imread('images/walking.jpg')

    img = rescal_frame(img,1)

    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos('H Min','TrackBars')
    h_max = cv.getTrackbarPos('H Max','TrackBars')

    s_min = cv.getTrackbarPos('S Min','TrackBars')
    s_max = cv.getTrackbarPos('S Max','TrackBars')

    v_min = cv.getTrackbarPos('V Min','TrackBars')
    v_max = cv.getTrackbarPos('V Max','TrackBars')

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv.inRange(hsv,lower,upper)
    fimg  = cv.bitwise_and(img,img,mask=mask)
    canny = cv.Canny(fimg, 150, 200)

    cv.imshow('canny image', canny)


    cv.imshow('image',img)
    cv.imshow('hsv',hsv)
    cv.imshow('mask',mask)
    cv.imshow('fimg',fimg)

    cv.waitKey(1)
