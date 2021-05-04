import numpy as np, cv2, math, random, time
from cmu_112_graphics import *
import collisions, objects
#ball file

# def appStarted(app):
#     initialConditions(app)
#     app.timerDelay = 1

def initialConditions(app):
    playWidth = app.width*4.5/7
    app.r = 6
    app.x0 = playWidth/2
    app.y0 = app.height/2
    app.vi = 5.2 # initial velocity
    app.angle = math.radians(45)
    app.yVel = app.vi * math.sin(app.angle)
    app.xVel = app.vi * math.cos(app.angle)
    app.dx = 0
    app.dy = 0
    app.gravity = 0.0098 # gravity in m/ms^2 since timerDelay is 1ms
    app.coeff_restitution = 0.94 # "bounciness" after a collision
    app.ballPos = [(playWidth/2, app.height/2)]
    # app.objectList = []
    # app.triPos = [(150, 100), (250, 220), (50, 160)]
    # app.paraPos = [(500, 100), (550, 150), (500, 200), (450, 150)]
    # app.rectPos = [(400, 400), (450, 400), (450, 440), (400, 440)]
    # app.objectList.append(app.triPos)
    # app.objectList.append(app.paraPos)
    # app.objectList.append(app.rectPos)

# def keyPressed(app, event):
#     if event.key=='x':
#         doStep(app)
    
def updateBall(app):
    doStep(app)
    isInFrame(app)
    app.ballPos.append((app.x0+app.r, app.y0+app.r))
    if len(app.ballPos)>2:
        app.ballPos.pop(0)
    flag, x1, y1, x2, y2 = isColliding(app)
    if flag:
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
    if x1==x2:
        b = 0
        a, c = -1, x1
    else:
        b = 1
        a, c = getEquationOfLine(x1, y1, x2, y2)
    # print(((abs(a * app.x0 + b * app.y0 + c)) / math.sqrt(a * a + b * b)))
    return ((abs(a * app.x0 + b * app.y0 + c)) / math.sqrt(a * a + b * b))

def getEquationOfLine(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    constant = y1-(slope*x1)
    # print(-slope, -constant)
    return -slope, -constant

def isLineBallColliding(app, x1, y1, x2, y2):
    r = app.r
    return ((distBetweenLineBall(app, x1, y1, x2, y2) <= r) 
            and ((min(x1, x2)-r)<app.x0<(max(x1, x2)+r))
            and ((min(y1, y2)-r)<app.y0<(max(y1, y2)+r)))

# def lineIsVertical(app):
#     pass

def isColliding(app):
    for item in app.objectDict:
        for points in app.objectDict[item]:
            for i in range(len(points)-1):
                x1, y1 = points[i]
                x2, y2 = points[i+1]
                if isLineBallColliding(app, x1, y1, x2, y2):
                    # print(True, x1, y1, x2, y2, app.x0, app.y0)
                    return (True, x1, y1, x2, y2)
            x1, y1 = points[0]
            x2, y2 = points[-1]
            if isLineBallColliding(app, x1, y1, x2, y2):
                    # print(True, x1, y1, x2, y2, app.x0, app.y0)
                    return (True, x1, y1, x2, y2)
    return (False, 0, 0, 0, 0)

# def isColliding(app):
#     for points in app.objectList:
#         for i in range(len(points)-1):
#             x1, y1 = points[i]
#             x2, y2 = points[i+1]
#             if isLineBallColliding(app, x1, y1, x2, y2):
#                 # print(True, x1, y1, x2, y2, app.x0, app.y0)
#                 return (True, x1, y1, x2, y2)
#         x1, y1 = points[0]
#         x2, y2 = points[-1]
#         if isLineBallColliding(app, x1, y1, x2, y2):
#                 # print(True, x1, y1, x2, y2, app.x0, app.y0)
#                 return (True, x1, y1, x2, y2)
#     return (False, 0, 0, 0, 0)
    



# def stopBall(app):
#     if app.yVel < 1 and 

def isInFrame(app):
    playWidth = app.width*4.5/7
    if app.x0+app.r>playWidth: 
        #right
        app.xVel *= -app.coeff_restitution
        app.x0 = playWidth-app.r
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
    y1, y2 = -y1, -y2
    if x1==x2:
        slope = math.radians(270)
    else:
        slope = math.atan((y2-y1)/(x2-x1))
    xNorm = -math.sin(slope)
    yNorm = -math.cos(slope)
    normBallDot = (app.xVel * xNorm) + (app.yVel * yNorm)
    app.xVel -= (2 * normBallDot * xNorm)
    app.yVel -= (2 * normBallDot * yNorm)


    


# def timerFired(app):
#     updateBall(app)

# def appStopped(app):
#     pass

# def drawCollisionBox(app, canvas):
#     for points in app.objectList:
#         canvas.create_polygon(points, fill = "blue")

def drawCircle(app, canvas):
    canvas.create_oval(app.x0-app.r, app.y0-app.r, 
                                    app.x0+app.r, app.y0+app.r,
                                    fill = "red")

# def redrawAll(app, canvas):
#     drawCircle(app, canvas)
#     drawCollisionBox(app, canvas)

# runApp(width = 650, height = 450)
