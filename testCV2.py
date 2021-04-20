import numpy as np, cv2, time, os
from cmu_112_graphics import *

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

def timerFired(app):
    singularBlue(app)

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text = str(app.isBlue))

def singularBlue(app):
    app.isBlue = False
    testVid = cv2.VideoCapture(0)
    testVid.set(3, 640)
    testVid.set(4, 480)
    testVid.set(10, 100)
    test, image = testVid.read()
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
        if area>7000:
            app.isBlue = True
    testVid.release()
    cv2.destroyAllWindows()
    
def blueDetection(app):
    app.isBlue = False
    testVid = cv2.VideoCapture(0)
    testVid.set(3, 640)
    testVid.set(4, 480)
    testVid.set(10, 100)
    while True:
        test, image = testVid.read()
        # image = cv2.Canny(image, 100, 100)
        # image = cv2.dilate(image, kernel, iterations = 1)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lowBlue = np.array([110,50,50])
        upBlue = np.array([130,255,255])
        mask = cv2.inRange(hsv, lowBlue, upBlue)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel)
        res = cv2.bitwise_and(image, image, mask=mask)
        contours, hierarchy = cv2.findContours(mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area>7000:
                app.isBlue = True
                cv2.waitKey(1)
                cv2.destroyAllWindows()
                for i in range (1,5):
                    cv2.waitKey(1)
                break
                # x, y, w, h = cv2.boundingRect(contour)
                # image = cv2.rectangle(image, (x, y), 
                #                         (x + w, y + h), 
                #                         (0, 0, 255), 2)
                # cv2.putText(image, "Blue Colour", (x, y),
                #             cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                #             (0, 0, 255))
        # if(app.isBlue):
        break
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
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            # cv2.waitKey(1)
            # cv2.destroyAllWindows()
            # for i in range (1,5):
            #     cv2.waitKey(1)
            # break

    testVid.release()
    cv2.destroyAllWindows()


runApp(width=400, height=400)


