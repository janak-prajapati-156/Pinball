import numpy as np, cv2, time, os
from cmu_112_graphics import *

#please go to the end of the code for the citations

# shrek = cv2.imread("images/shrek.png", 1)
# shrekBlur = cv2.GaussianBlur(shrek, (7, 7), (0))
# kernel = np.ones((5, 5), np.uint8)
# print(kernel)
# shrekEdge = cv2.Canny(shrek, 100, 100)
# shrekDil = cv2.dilate(shrekEdge, kernel, iterations = 1)
# cv2.imshow("output", shrekDil)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# testVid = cv2.VideoCapture("images/testVideo.mov")

def appStarted(app):
    app.isBlue = False
    app.testVid = cv2.VideoCapture(0)
    # singularBlue(app)

def timerFired(app):
    # finalSingularBlue(app)
    pass

def appStopped(app):
    app.testVid.release()
    cv2.destroyAllWindows()

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text = str(app.isBlue))

def finalSingularBlue(app):
    test, image = app.testVid.read()
    image = cv2.flip(image, 1)
    areaList = []
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # lowYellow = np.array([16, 100, 100])
    # upYellow = np.array([32, 255, 255])
    lowBlue = np.array([110,50,50])
    upBlue = np.array([130,255,255])
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
    cv2.imshow("output", image)

def singularBlue(app):
    app.isBlue = False
    app.testVid = cv2.VideoCapture(0)
    while testVid.isOpened():
        test, image = testVid.read()
        image = cv2.flip(image, 1)
        areaList = []
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lowBlue = np.array([110,50,50])
        upBlue = np.array([130,255,255])
        mask = cv2.inRange(hsv, lowBlue, upBlue)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel)
        res = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, 
                                                cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            areaList.append(area)
        if areaList!=[] and max(areaList)>7000:
            app.isBlue = True
        else:
            app.isBlue = False
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            for i in range (1,5):
                cv2.waitKey(1)
            break
    testVid.release()
    cv2.destroyAllWindows()
    
def blueDetection():
    # a large part of this was copied
    check = False
    testVid = cv2.VideoCapture(0)
    # testVid.set(3, 640)
    # testVid.set(4, 480)
    # testVid.set(10, 100)
    while True:
        test, image = testVid.read()
        areaList = []
        image = cv2.flip(image, 1)
        # print(testVid.isOpened())
        # image = cv2.Canny(image, 100, 100)
        # image = cv2.dilate(image, kernel, iterations = 1)
        # green_lower = np.array([25, 52, 72], np.uint8)
        # green_upper = np.array([102, 255, 255], np.uint8)
        red_lower = np.array([136, 87, 111], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)
        # (0-179 degrees (360), 0-255 saturation (100%), 0-255 value (100%))
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # lowYellow = np.array([16, 100, 100])
        # upYellow = np.array([32, 255, 255])
        lowOrange = np.array([5, 50, 50])
        upOrange = np.array([15, 255, 255])
        mask = cv2.inRange(hsv, red_lower, red_upper)
        # lowBlue = np.array([110,50,50])
        # upBlue = np.array([130,255,255])
        # mask = cv2.inRange(hsv, lowBlue, upBlue)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel)
        res = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            areaList.append(area)
            if area>10000:
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), 
                                        (x + w, y + h), 
                                        (0, 0, 255), 2)
                cv2.putText(image, "Blue Colour", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (0, 0, 255))

        # if areaList!=[] and max(areaList)>7000:
        #     print(True)
        # else:
        #     print(False)
        # b = res[:, :, :1]
        # g = res[:, :, 1:2]
        # r = res[:, :, 2:]
        # bmean = np.mean(b)
        # gmean = np.mean(g)
        # rmean = np.mean(r)
        # if bmean>gmean and bmean>rmean:
        #     print("blue")
        # elif (gmean > rmean and gmean > bmean):
        #     print("Green")
        # else:
        #     print("Red")

        cv2.imshow("output", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            for i in range (1,5):
                cv2.waitKey(1)
            break

    testVid.release()
    cv2.destroyAllWindows()

blueDetection()
# runApp(width=400, height=400)

"""
Citations:
OpenCV code for loading image - https://www.youtube.com/watch?v=WQeoO7MI0Bs

learning how to use the webcam :
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
did not copy the code, understood the code first and then wrote it myself

configuring vscode to access the webcam :
https://rajathithanrajasekar.medium.com/opencv-series-2-configure-vscode-for-opencv-development-in-macos-4a2a06e144fa

detecting colors in opencv:
https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/
a large part of blueDetection() is copied from this website
singularBlue() and finalSingularBlue() were written from scratch 
"""
