import numpy as np, cv2, math, random
from cmu_112_graphics import *
import objects, ball

def appStarted(app):
    objects.initialisePoints(app)
    ball.initialConditions(app)
    app.timerDelay = 1

def timerFired(app):
    ball.updateBall(app)

def redrawAll(app, canvas):
    objects.triangularBox(app, canvas)
    objects.sectionLine(app, canvas)
    objects.drawEdge(app, canvas)
    ball.drawCircle(app, canvas)

runApp(width=700, height=800)