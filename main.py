import numpy as np, cv2, math, random
from cmu_112_graphics import *
import objects, ball, opencv, sidebar

def appStarted(app):
    startGame(app)

def startGame(app):
    objects.initialisePoints(app)
    ball.initialConditions(app)
    opencv.initialCV(app)
    app.timerDelay = 1
    app.oldH = app.height*6.66/8
    app.newH = app.height*7.5/8
    app.currH = app.height*6.66/8
    app.currH2 = app.height*6.66/8
    app.diffH = (app.newH-app.oldH)/15

def appStopped(app):
    app.testVid.release()
    cv2.destroyAllWindows()

def keyPressed(app, event):
    playWidth = app.width*4.5/7
    if event.key=='a' or event.key=='Left':
        app.isRed = True
    if event.key=='d' or event.key=='Right':
        app.isBlue = True
    if event.key=='r':
        startGame(app)
    if event.key=='Space' and app.spaceCount<1:
        app.gameOver = False
        app.spaceCount+=1
    if event.key=='q':
        app.gameOver = True

def keyReleased(app, event):
    playWidth = app.width*4.5/7
    if event.key=='a' or event.key=="Left":
        app.isRed = False
    if event.key=='d' or event.key=="Right":
        app.isBlue = False

def flipperMoveFinal(app):
    playWidth = app.width*4.5/7
    if not app.isBlue:
        if app.currH<app.newH:
            app.currH += app.diffH
            app.objectDict['flipper'][1] = [(playWidth*7.25/9, app.height*7.08/8), 
            (playWidth*2.75/5, app.currH), (playWidth*2.75/5, app.currH + app.height*.18/8),
            (playWidth*7.15/9, app.height*7.26/8)]
    else:
        if app.currH>app.oldH:
            app.currH -= app.diffH
            app.objectDict['flipper'][1] = [(playWidth*7.25/9, app.height*7.08/8), 
            (playWidth*2.75/5, app.currH), (playWidth*2.75/5, app.currH+ app.height*.18/8),
            (playWidth*7.15/9, app.height*7.26/8)]

    if not app.isRed:
        if app.currH2<app.newH:
            app.currH2 += app.diffH
            app.objectDict['flipper'][0] = [(playWidth*1.75/9, app.height*7.08/8), 
                (playWidth*2.25/5, app.currH2), (playWidth*2.25/5, app.currH2 + app.height*.18/8),
                (playWidth*1.85/9, app.height*7.26/8)]
    else:
        if app.currH2>app.oldH:
            app.currH2 -= app.diffH
            app.objectDict['flipper'][0] = [(playWidth*1.75/9, app.height*7.08/8), 
                (playWidth*2.25/5, app.currH2), (playWidth*2.25/5, app.currH2 + app.height*.18/8),
                (playWidth*1.75/9, app.height*7.26/8)]

# def flipperMove(app):
#     playWidth = app.width*4.5/7
#     if app.isBlue:
#         app.objectDict['flipper'][1] = [(playWidth*7.25/9, app.height*7.08/8), 
#             (playWidth*2.75/5, app.height*6.66/8), 
#             (playWidth*7.15/9, app.height*7.26/8)]
#     else:
#         app.objectDict['flipper'][1] = [(playWidth*7.25/9, app.height*7.08/8), 
#             (playWidth*2.75/5, app.height*7.5/8), 
#             (playWidth*7.25/9, app.height*7.26/8)]
#     if app.isRed:
#         app.objectDict['flipper'][0] = [(playWidth*1.75/9, app.height*7.08/8), 
#             (playWidth*2.25/5, app.height*6.66/8), 
#             (playWidth*1.85/9, app.height*7.26/8)]
#     else:
#         app.objectDict['flipper'][0] = [(playWidth*1.75/9, app.height*7.08/8), 
#             (playWidth*2.25/5, app.height*7.5/8), 
#             (playWidth*1.75/9, app.height*7.26/8)]


def timerFired(app):
    if app.gameOver: return
    ball.updateBall(app)
    opencv.finalSingularRed(app)
    opencv.finalSingularBlue(app)
    flipperMoveFinal(app)

def redrawAll(app, canvas):
    objects.triangularBox(app, canvas)
    objects.sectionLine(app, canvas)
    objects.drawEdge(app, canvas)
    objects.flipper(app, canvas)
    objects.rhombus(app, canvas)
    objects.parallelogram(app, canvas)
    sidebar.drawInstructions(app, canvas)
    sidebar.drawScore(app, canvas)
    ball.drawCircle(app, canvas)

runApp(width=700, height=750)