import numpy as np, cv2, math, random, time
# from cmu_112_graphics import *
#collisions

def linesCollide(x1, y1, x2, y2, a1, b1, a2, b2):
    orientations = []
    orientations.append(orientation(x1, y1, x2, y2, a1, b1))
    orientations.append(orientation(x1, y1, x2, y2, a2, b2))
    orientations.append(orientation(a1, b1, a2, b2, x1, y1))
    orientations.append(orientation(a1, b1, a2, b2, x2, y2))
    if orientations[0]!= orientations[1] and orientations[2]!=orientations[3]:
        return True
    if orientations[0]=='linear' and isOnLine(x1, y1, x2, y2, a1, b1):
        return True
    elif orientations[1]=='linear' and isOnLine(x1, y1, x2, y2, a2, b2):
        return True
    elif orientations[2]=='linear' and isOnLine(a1, b1, a2, b2, x1, y1):
        return True
    elif orientations[3]=='linear' and isOnLine(a1, b1, a2, b2, x2, y2):
        return True
    return False

def isOnLine(x1, y1, x2, y2, a1, b1):
    #check if point a1b1 is on line x1y1-x2y2
    if ((a1<=max(x1, x2)) and (a1>=min(x1, x2)) 
        and (b1<=max(y1, y2)) and (b2>=min(y1, y2))):
        return True
    return False

def orientation(x1, y1, x2, y2, x3, y3):
    #calculating what direction the 3 points are in using their slopes
    slope = ((y2-y1) * (y3-y2)) - ((x2-x1) * (x3-x2))
    #slope positive: anti-clockwise
    #slope negative: clockwise
    #slope = 0: linear
    if slope>0:
        return 'anti-clockwise'
    elif slope<0:
        return 'clockwise'
    else:
        return 'linear'

def distBetweenLineBall(x1, y1, x2, y2):
    x0, y0 = 400, 400
    if x1==x2:
        b = 0
        a, c = -1, 400
    else:
        b = 1
        a, c = getEquationOfLine(x1, y1, x2, y2)
    print(((abs(a * x0 + b * y0 + c)) / math.sqrt(a * a + b * b)))
    return ((abs(a * x0 + b * y0 + c)) / math.sqrt(a * a + b * b))

def getEquationOfLine(x1, y1, x2, y2):
    slope = (y2-y1)/(x2-x1)
    constant = y1-(slope*x1)
    print(-slope, -constant)
    return -slope, -constant

def isLineBallColliding(x1, y1, x2, y2):
    r = 20
    x0, y0 = 400, 400
    return ((distBetweenLineBall(x1, y1, x2, y2) <= r) 
            and ((min(x1, x2)-r)<x0<(max(x1, x2)+r))
            and ((min(y1, y2)-r)<y0<(max(y1, y2)+r)))

# print(isLineBallColliding(400, 400, 400, 450))


# def vectorCalc():
#     # angle = -45
#     vx, vy = 0, 1
#     x1, y1, x2, y2 = 0, 0, 1, -1
#     # nx = -math.sin(math.radians(angle))
#     # ny = -math.cos(math.radians(angle))
#     nx = -math.sin(math.atan((y2-y1)/(x2-x1)))
#     ny = -math.cos(math.atan((y2-y1)/(x2-x1)))
#     dot = vx * nx + vy * ny
#     vnewx = vx - (2 * dot * nx)
#     vnewy = vy - (2 * dot * ny)
#     print(nx, ny)
#     print(vx, vy)
#     print(vnewx, vnewy)

# vectorCalc()


# def getAngle(x1, y1, x2, y2):
#     # x1, x2, y1, y2 = 150, 100, 250, 160
#     slope = (y2-y1)/(x2-x1)
#     angle = math.degrees(math.atan(slope))
#     return angle

# # print(getAngle(150, -100, 250, -160))

def vectorCalc2(x1, y1, x2, y2):
    if x1==x2:
        slope = math.radians(270)
    else:
        slope = math.atan((y2-y1)/(x2-x1))
    
    xVel, yVel = 1, 0
    xNorm = -math.sin(slope)
    yNorm = -math.cos(slope)
    print(xNorm, yNorm)
    print(xVel, yVel)
    normBallDot = (xVel * xNorm) + (yVel * yNorm)
    xVel -= (2 * normBallDot * xNorm)
    yVel -= (2 * normBallDot * yNorm)
    print(xVel, yVel)

# vectorCalc2(0, 0, 0, 1)
