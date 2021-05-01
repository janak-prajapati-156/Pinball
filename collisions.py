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
