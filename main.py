import numpy as np, cv2, math, random
from cmu_112_graphics import *
import objects, ball, opencv, sidebar

def appStarted(app):
    # name = input('Name:')
    startGame(app)

def startGame(app):
    objects.initialisePoints(app)
    ball.initialConditions(app)
    opencv.initialCV(app)
    app.scorelist = []
    app.username = None
    sidebar.keepScores(app)
    app.timerDelay = 1
    # app.background = app.loadImage('background.jpg')

def appStopped(app):
    app.testVid.release()
    cv2.destroyAllWindows()

# def mousePressed(app, event):
#     if app.username==None:
#         app.username = input('Enter your name : ')
#         # name = app.getUserInput('What is your name?')
#         # app.username = name

def keyPressed(app, event):
    playWidth = app.width*4.5/7
    # if event.key=='Enter' and app.username==None:
    #     app.username = app.getUserInput("Please enter your name")
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

def timerFired(app):
    if app.gameOver: return
    ball.updateBall(app)
    opencv.finalSingularRed(app)
    opencv.finalSingularBlue(app)
    objects.flipperMoveFinal(app)

def redrawAll(app, canvas):
    # canvas.create_image(900, 1500, image = ImageTk.PhotoImage(app.background))
    playWidth = app.width*4.5/7
    objects.triangularBox(app, canvas)
    objects.sectionLine(app, canvas)
    objects.drawEdge(app, canvas)
    objects.flipper(app, canvas)
    objects.rhombus(app, canvas)
    objects.parallelogram(app, canvas)
    sidebar.drawInstructions(app, canvas)
    sidebar.drawScore(app, canvas)
    sidebar.highscores(app, canvas)
    ball.drawCircle(app, canvas)
    if app.gameOver and app.spaceCount>0:
        canvas.create_text((playWidth+app.width)/2, (app.height/2) + 20, 
                        text = f"Game Over!", font = 'Helvetica 16')

runApp(width=700, height=750)