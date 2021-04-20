import numpy as np, cv2, math, random
from cmu_112_graphics import *
import testCV2

# class pinball(object):
#     def __init__(self):
#         self.radius = "janak"

def appStarted(app):
    app.isBlue = False
    app.testVid = cv2.VideoCapture(0)
    # app.testVid.set(3, 650)
    # app.testVid.set(4, 450)
    app.r = 30
    app.cx = random.randint(app.r, app.width-app.r)
    app.cy = random.randint(app.r, app.height-app.r)
    app.dx = 2
    app.dy = 4
    app.velocity = 5
    app.gameOver = False

def keyPressed(app, event):
    if event.key=='s':
        app.dx *= 2
        app.dy *= 2

def inCircle(app, x1, y1):
    return math.sqrt((app.cx-x1)**2 + (app.cy-y1)**2) < app.r

def mousePressed(app, event):
    pass


def isInFrame(app):
    if (app.cx+app.r>=app.width or app.cx-app.r<=0):
        app.dx = -app.dx
    if (app.cy+app.r>=app.height or app.cy-app.r<=0):
        app.dy = -app.dy

def timerFired(app):
    testCV2.finalSingularBlue(app)
    isInFrame(app)
    if app.isBlue:
        app.cx += app.dx
        app.cy += app.dy
    

def appStopped(app):
    app.testVid.release()
    cv2.destroyAllWindows()

def drawCircle(app, canvas):
    canvas.create_oval(app.cx-app.r, app.cy-app.r, app.cx+app.r, app.cy+app.r,
                        fill = "red")
    canvas.create_text(app.width/2, app.height/2, text = str(app.isBlue))

def redrawAll(app, canvas):
    drawCircle(app, canvas)

runApp(width=650, height=450)
# testCV2.blueDetection()