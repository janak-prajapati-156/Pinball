import numpy as np, cv2, math, random
from cmu_112_graphics import *
import testCV2

def appStarted(app):
    app.isBlue = False
    app.testVid = cv2.VideoCapture(0)
    # app.testVid.set(3, 650)
    # app.testVid.set(4, 450)

def keyPressed(app, event):
    pass

def mousePressed(app, event):
    pass


def timerFired(app):
    testCV2.finalSingularBlue(app)

def appStopped(app):
    app.testVid.release()
    cv2.destroyAllWindows()


def redrawAll(app, canvas):
    pass

runApp(width=650, height=450)
# testCV2.blueDetection()