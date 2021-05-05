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
    app.kernel = np.ones((5, 5), np.uint8)
    app.lowBlue = np.array([110,50,50], np.uint8)
    app.upBlue = np.array([130,255,255], np.uint8)
    app.lowRed = np.array([136, 87, 111], np.uint8)
    app.upRed = np.array([180, 255, 255], np.uint8)
    app.testVid = cv2.VideoCapture(0)
    app.testVid.set(3, 600)
    app.testVid.set(4, 400)

def finalSingularBlue(app):
    test, image = app.testVid.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, app.lowBlue, app.upBlue)
    mask = cv2.dilate(mask, app.kernel)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area>10000:
            app.isBlue = True
            return
    app.isBlue = False
    # cv2.imshow("output", image)

def finalSingularRed(app):
    test, image = app.testVid.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, app.lowRed, app.upRed)
    mask = cv2.dilate(mask, app.kernel)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, 
                                            cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area>10000:
            app.isRed = True
            return
    app.isRed = False

"""
A part of this code is editted from the code found @
“Multiple Color Detection in Real-Time Using Python-OpenCV - GeeksforGeeks.” GeeksforGeeks, 24 Apr. 2020, www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/. Accessed 20 Apr. 2021.

“Python Programming Tutorials.” Pythonprogramming.net, 2021, pythonprogramming.net/morphological-transformation-python-opencv-tutorial/. Accessed 20 Apr. 2021.


Canu, Sergio. “Detecting Colors (Hsv Color Space) - Opencv with Python - Pysource.” Pysource, 15 Feb. 2019, pysource.com/2019/02/15/detecting-colors-hsv-color-space-opencv-with-python/. Accessed 20 Apr. 2021.

“YaflaColor RGB - HSV Color Conversion.” Archive.org, 2012, web.archive.org/web/20130806191424/www.yafla.com/yaflacolor/ColorRGBHSL.html. Accessed 20 Apr. 2021

"""