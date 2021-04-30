import numpy as np, cv2, math, random, time
from cmu_112_graphics import *
#ball file

def appStarted(app):
    initialConditions(app)
    app.timerDelay = 1

def initialConditions(app):
    app.r = 20
    app.x0 = app.width/2
    app.y0 = app.height/2
    app.vi = 1 # initial velocity
    app.angle = math.radians(0)
    app.yVel = app.vi * math.sin(app.angle)
    app.xVel = app.vi * math.cos(app.angle)
    app.dx = 0
    app.dy = 0
    app.gravity = 0.0098 # gravity in m/ms since timerDelay is 1ms
    app.coeff_restitution = 0.94 # "bounciness" after a collision
    app.ballPos = []
    app.rectPos = [app.r, app.r, app.r*5, app.r*5]

def keyPressed(app, event):
    if event.key=='x':
        print(getAngle(app))

def updateBall(app):
    #update ball is called every one second so standard m/s calc can be made
    app.dx = app.xVel
    #x-direction isn't affected by gravity
    app.yVel += app.gravity
    #since the y-cord are inverted in canvas, we add the gravity to the vel
    app.dy = app.yVel
    #change per second is the new velocity
    app.x0 += app.dx
    app.y0 += app.dy
    isInFrame(app)
    app.ballPos.append((app.x0, app.y0))
    if len(app.ballPos)>2:
        app.ballPos.pop(0)

def isColliding(app):
    xR1, yR1, xR2, yR2 = app.restPos
    if xR1<=app.x0<=xR2 and yR1<=app.y0<=yR2:
        angle = getAngle(app)


# def stopBall(app):
#     if app.yVel < 1 and 

def isInFrame(app):
    if app.x0+app.r>app.width: 
        #right
        app.xVel *= -app.coeff_restitution
        app.x0 = app.width-app.r
    if app.x0-app.r<0:
        #left
        app.xVel *= -app.coeff_restitution
        app.x0 = app.r
    if app.y0-app.r<0: 
        #top
        app.yVel *= -app.coeff_restitution
        app.y0 = app.r
    if app.y0+app.r>app.height: 
        #bottom
        app.yVel *= -app.coeff_restitution
        app.y0 = app.height-app.r

def getAngle(app):
    x1, y1 = app.ballPos[0]
    x2, y2 = app.ballPos[1]
    slope = (y2-y1)/(x2-x1)
    angle = math.degrees(math.atan(slope))
    return angle


def timerFired(app):
    updateBall(app)

# def appStopped(app):
#     getAngle(app)

def drawCollisionBox(app, canvas):
    canvas.create_rectangle(app.r, app.r, app.r*5, app.r*5, fill = "blue")

def drawCircle(app, canvas):
    canvas.create_oval(app.x0-app.r, app.y0-app.r, 
                                    app.x0+app.r, app.y0+app.r,
                                    fill = "red")

def redrawAll(app, canvas):
    drawCircle(app, canvas)
    drawCollisionBox(app, canvas)

runApp(width = 650, height = 450)

"""
TokyoEdtech. “Python Bouncing Ball Simulator 2.” YouTube, 12 June 2018, www.youtube.com/watch?v=ibdICVK0W3Q. Accessed 26 Apr. 2021.

‌“Projectile Motion Formula.” 101 Computing, 3 July 2014, www.101computing.net/projectile-motion-formula/. Accessed 26 Apr. 2021.

‌
"""