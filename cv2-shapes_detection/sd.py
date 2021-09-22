import cv2
import numpy as np



def getPolyContours(img):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    polygons = {3:'Triangle',4:'Rectangle',5:'Pentagon',8:'Circle'}

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            objectType = polygons[objCor]
            print(objectType)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (140, 140, 140), 3)
            cv2.putText(imgContour, objectType,(x , y ), cv2.FONT_HERSHEY_COMPLEX, 0.6,(0, 0, 0),1)



path = 'images/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getPolyContours(imgCanny)


cv2.imshow("img", img)
cv2.imshow("imgContour", imgContour)


cv2.waitKey(0)