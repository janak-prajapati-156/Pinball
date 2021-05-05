import numpy as np, cv2, math, random, time
from cmu_112_graphics import *
import objects
#ball file

# def appStarted(app):
#     initialConditions(app)
#     app.timerDelay = 1

def initialConditions(app):
    playWidth = app.width*4.5/7
    app.gameOver = True
    app.spaceCount = 0
    app.r = 6
    app.x0 = playWidth/2
    app.y0 = app.height/2
    app.vi = 4 # initial velocity
    app.angle = math.radians(80)
    app.yVel = app.vi * math.sin(app.angle)
    app.xVel = app.vi * math.cos(app.angle)
    app.dx = 0
    app.dy = 0
    app.gravity = 0.0098 # gravity in m/ms^2 since timerDelay is 1ms
    app.coeff_restitution = 0.94 # "bounciness" after a collision
    app.ballPos = [(playWidth/2, app.height/2)]
    app.score = 0
    
def updateBall(app):
    doStep(app)
    isInFrame(app)
    app.ballPos.append((app.x0+app.r, app.y0+app.r))
    if len(app.ballPos)>2:
        app.ballPos.pop(0)
    flag, x1, y1, x2, y2 = isColliding(app)
    if flag:
        app.score += 3
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
    return ((abs(a * app.x0 + b * app.y0 + c)) / math.sqrt(a * a + b * b))

def getEquationOfLine(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    constant = y1-(slope*x1)
    return -slope, -constant

def isLineBallColliding(app, x1, y1, x2, y2):
    r = app.r
    return ((distBetweenLineBall(app, x1, y1, x2, y2) <= r) 
            and ((min(x1, x2)-r)<app.x0<(max(x1, x2)+r))
            and ((min(y1, y2)-r)<app.y0<(max(y1, y2)+r)))

def isColliding(app):
    for item in app.objectDict:
        for points in app.objectDict[item]:
            for i in range(len(points)-1):
                x1, y1 = points[i]
                x2, y2 = points[i+1]
                if isLineBallColliding(app, x1, y1, x2, y2):
                    return (True, x1, y1, x2, y2)
            x1, y1 = points[0]
            x2, y2 = points[-1]
            if isLineBallColliding(app, x1, y1, x2, y2):
                    return (True, x1, y1, x2, y2)
    return (False, 0, 0, 0, 0)

def isInFrame(app):
    playWidth = app.width*4.5/7
    if app.x0+app.r>playWidth: 
        #right
        app.xVel *= -app.coeff_restitution
        app.x0 = playWidth-app.r
        app.score += 1
    if app.x0-app.r<0:
        #left
        app.xVel *= -app.coeff_restitution
        app.x0 = app.r
        app.score += 1
    if app.y0-app.r<0: 
        #top
        app.yVel *= -app.coeff_restitution
        app.y0 = app.r
        app.score += 1
    if app.y0+app.r>app.height: 
        #bottom
        # app.yVel *= -app.coeff_restitution
        # app.y0 = app.height-app.r
        app.gameOver = True

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

def drawCircle(app, canvas):
    canvas.create_oval(app.x0-app.r, app.y0-app.r, 
                                    app.x0+app.r, app.y0+app.r,
                                    fill = "red")

"""
the algorithm for collision detection was learnt from 
“How to Check If a given Point Lies inside or Outside a Polygon? - GeeksforGeeks.” GeeksforGeeks, 11 July 2013, www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/#:~:text=1)%20Draw%20a%20horizontal%20line,true%2C%20then%20point%20lies%20outside.. Accessed 1 May 2021.

“How to Check If Two given Line Segments Intersect? - GeeksforGeeks.” GeeksforGeeks, 10 July 2013, www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/. Accessed 1 May 2021.

“Intersection of a Line and a Circle.” DoubleRoot.in, Dec. 2020, doubleroot.in/lessons/circle/intersection-line-circle-1/#:~:text=To%20determine%20the%20position%20of,circle%20at%20two%20distinct%20points.. Accessed 1 May 2021.

“Check If a Line Touches or Intersects a Circle - GeeksforGeeks.” GeeksforGeeks, 17 Sept. 2017, www.geeksforgeeks.org/check-line-touches-intersects-circle/. Accessed 1 May 2021.

The vectorcalc was learnt from:
Batash. “Calculate Angle Change after Hitting a Tilted Wall.” Stack Overflow, 17 July 2017, stackoverflow.com/questions/45154176/calculate-angle-change-after-hitting-a-tilted-wall. Accessed 1 May 2021.

“Dot Product.” Mathsisfun.com, 2017, www.mathsisfun.com/algebra/vectors-dot-product.html. Accessed 1 May 2021.


The ball's motion was learnt from:
“Projectile Motion Formula.” 101 Computing, 3 July 2014, www.101computing.net/projectile-motion-formula/. Accessed 26 Apr. 2021.

TokyoEdtech. “Python Bouncing Ball Simulator 2.” YouTube, 12 June 2018, www.youtube.com/watch?v=ibdICVK0W3Q. Accessed 26 Apr. 2021

"""