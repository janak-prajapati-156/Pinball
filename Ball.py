import numpy as np, cv2, math, random, time
from cmu_112_graphics import *
import collisions
#ball file

def appStarted(app):
    initialConditions(app)
    app.timerDelay = 1

def initialConditions(app):
    app.r = 5
    app.x0 = app.width/2
    app.y0 = app.height/2
    app.vi = 3 # initial velocity
    app.angle = math.radians(70)
    app.yVel = app.vi * math.sin(app.angle)
    app.xVel = app.vi * math.cos(app.angle)
    app.dx = 0
    app.dy = 0
    app.gravity = 0.0098 # gravity in m/ms^2 since timerDelay is 1ms
    app.coeff_restitution = 0.94 # "bounciness" after a collision
    app.ballPos = [(app.width/2, app.height/2)]
    app.triPos = [(150, 100), (250, 160), (50, 160)]

def keyPressed(app, event):
    if event.key=='x':
        doStep(app)
    
def updateBall(app):
    doStep(app)
    isInFrame(app)
    app.ballPos.append((app.x0+app.r, app.y0+app.r))
    if len(app.ballPos)>2:
        app.ballPos.pop(0)
    flag, x1, y1, x2, y2 = isColliding(app)
    if flag:
        print(x1, y1, x2, y2, app.x0, app.y0)
        vectorCalc(app, x1, y1, x2, y2)
        doStep(app)

def doStep(app):
    app.dx = app.xVel
    #x-direction isn't affected by gravity
    app.yVel += app.gravity
    #since the y-cord are inverted in canvas, we add the gravity to the vel
    app.dy = app.yVel
    #change per second is the new velocity
    app.x0 += app.dx
    app.y0 += app.dy

def distBetweenLineBall(app, x1, y1, x2, y2):
    a = 1
    b, c = getEquationOfLine(x1, y1, x2, y2)
    return abs((b*app.x0) + (a*app.y0) + (c)) / math.sqrt((a*a) + (b*b))

def getEquationOfLine(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    constant = (slope*(0-x1) + y1)
    return slope, -constant

def isLineBallColliding(app, x1, y1, x2, y2):
    return ((distBetweenLineBall(app, x1, y1, x2, y2) <= app.r) 
            and ((min(x1, x2)-app.r)<app.x0<(max(x1, x2)+app.r))
            and ((min(y1, y2)-app.r)<app.y0<(max(y1, y2)+app.r)))

def isColliding(app):
    for i in range(len(app.triPos)-1):
        x1, y1 = app.triPos[i]
        x2, y2 = app.triPos[i+1]
        if isLineBallColliding(app, x1, y1, x2, y2):
            return (True, x1, y1, x2, y2)
    x1, y1 = app.triPos[0]
    x2, y2 = app.triPos[-1]
    if isLineBallColliding(app, x1, y1, x2, y2):
            return (True, x1, y1, x2, y2)
    return (False, 0, 0, 0, 0)
    



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

# def getAngle(x1, y1, x2, y2):
#     slope = (y2-y1)/(x2-x1)
#     angle = math.degrees(math.atan(slope))
#     return angle

def vectorCalc(app, x1, y1, x2, y2):
    xNorm = -math.sin(math.atan((y2-y1)/(x2-x1)))
    yNorm = -math.cos(math.atan((y2-y1)/(x2-x1)))
    normBallDot = (app.xVel * xNorm) + (app.yVel * yNorm)
    app.xVel -= (2 * normBallDot * xNorm)
    app.yVel -= (2 * normBallDot * yNorm)


    


def timerFired(app):
    updateBall(app)

# def appStopped(app):
#     pass

def drawCollisionBox(app, canvas):
    canvas.create_polygon(app.triPos, fill = "blue")

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