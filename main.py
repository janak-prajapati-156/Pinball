import numpy as np, cv2, math, random
from cmu_112_graphics import *
import objects, ball, opencv

def appStarted(app):
    objects.initialisePoints(app)
    ball.initialConditions(app)
    opencv.initialCV(app)
    app.timerDelay = 1

def appStopped(app):
    app.testVid.release()
    cv2.destroyAllWindows()

def keyPressed(app, event):
    playWidth = app.width*4.5/7
    if event.key=='a' or event.key=='Left':
        app.isBlue = True
    if event.key=='d' or event.key=='Right':
        app.isRed = True

def keyReleased(app, event):
    playWidth = app.width*4.5/7
    if event.key=='a' or event.key=="Left":
        app.isBlue = False
    if event.key=='d' or event.key=="Right":
        app.isRed = False

def flipperMove(app):
    playWidth = app.width*4.5/7
    if app.isBlue:
        app.objectDict['flipper'][1] = [(playWidth*7.25/9, app.height*7.08/8), 
            (playWidth*2.75/5, app.height*6.66/8), 
            (playWidth*7.15/9, app.height*7.26/8)]
    else:
        app.objectDict['flipper'][1] = [(playWidth*7.25/9, app.height*7.08/8), 
            (playWidth*2.75/5, app.height*7.5/8), 
            (playWidth*7.25/9, app.height*7.26/8)]
    if app.isRed:
        app.objectDict['flipper'][0] = [(playWidth*1.75/9, app.height*7.08/8), 
            (playWidth*2.25/5, app.height*6.66/8), 
            (playWidth*1.85/9, app.height*7.26/8)]
    else:
        app.objectDict['flipper'][0] = [(playWidth*1.75/9, app.height*7.08/8), 
            (playWidth*2.25/5, app.height*7.5/8), 
            (playWidth*1.75/9, app.height*7.26/8)]


def timerFired(app):
    if app.gameOver: return
    ball.updateBall(app)
    opencv.finalSingularRed(app)
    opencv.finalSingularBlue(app)
    flipperMove(app)

def redrawAll(app, canvas):
    objects.triangularBox(app, canvas)
    objects.sectionLine(app, canvas)
    objects.drawEdge(app, canvas)
    objects.flipper(app, canvas)
    ball.drawCircle(app, canvas)

runApp(width=700, height=750)