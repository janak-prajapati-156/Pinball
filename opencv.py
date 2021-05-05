import numpy as np, cv2, time, os
from cmu_112_graphics import *
#CV2 file

# def appStarted(app):
    # app.isBlue = False
    # app.isRed = False
    # app.testVid = cv2.VideoCapture(0)

def initialCV(app):
    app.isBlue = False
    app.isRed = False
    app.testVid = cv2.VideoCapture(0)


# def timerFired(app):
#     finalSingularRed(app)
#     finalSingularBlue(app)

# def appStopped(app):
#     app.testVid.release()
#     cv2.destroyAllWindows()

def finalSingularBlue(app):
    test, image = app.testVid.read()
    # image = cv2.flip(image, 1)
    areaList = []
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowBlue = np.array([110,50,50], np.uint8)
    upBlue = np.array([130,255,255], np.uint8)
    mask = cv2.inRange(hsv, lowBlue, upBlue)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel)
    res = cv2.bitwise_and(image, image, mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        areaList.append(area)
    if areaList!=[] and max(areaList)>10000:
        app.isBlue = True
    else:
        app.isBlue = False
    # cv2.imshow("output", image)

def finalSingularRed(app):
    test, image = app.testVid.read()
    # image = cv2.flip(image, 1)
    areaList = []
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowRed = np.array([136, 87, 111], np.uint8)
    upRed = np.array([180, 255, 255], np.uint8)
    mask = cv2.inRange(hsv, lowRed, upRed)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel)
    res = cv2.bitwise_and(image, image, mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        areaList.append(area)
    if areaList!=[] and max(areaList)>10000:
        app.isRed = True
    else:
        app.isRed = False
    # cv2.imshow("output", image)

