import numpy as np, cv2, math, random, time
from cmu_112_graphics import *
#ball file

def appStarted(app):
    app.r = 30
    app.x0 = app.width/2
    app.y0 = app.height/2
    app.vi = 0
    app.angle = 90
    app.vx = app.vi * math.cos(math.radians(app.angle))
    app.vy = app.vi * math.sin(math.radians(app.angle))
    app.ax = 0
    app.ay = 13
    app.dt = 0.05
    app.time = 0
    app.startTime = time.time()
    app.dx = 0
    app.dy = 0
    app.sX, app.sY = 1, 1
    app.flag = False

def updateVx(app):
    app.vx = app.vx + app.sX*(app.ax*app.dt)
    return app.vx

def updateVy(app):
    app.vy = app.vy + app.sY*(app.ay*app.dt)
    return app.vy

def updateX(app):
    app.dx = ((updateVx(app)*app.time) + (0.5*app.ax*app.time*app.time))
    app.x0 += app.dx

def updateY(app):
    app.dy = ((updateVy(app)*app.time) + (0.5*app.ay*app.time*app.time))
    app.y0 += app.dy

def keyPressed(app, event):
    if event.key=='x':
        app.flag = not app.flag
    if event.key=='s':
        app.vi *= 2

def inCircle(app, x1, y1):
    return math.sqrt((app.x0-x1)**2 + (app.y0-y1)**2) < app.r

def isInFrame(app):
    if (app.x0+app.r>=app.width or app.x0-app.r<=0):
        app.vx = -app.vx
    if app.y0+app.r>=app.height or app.y0-app.r<=0:
        app.sY = -1

def timerFired(app):
    if app.flag: return
    if time.time()-app.startTime > app.dt:
        isInFrame(app)
        app.time += app.dt
        updateX(app)
        updateY(app)
        app.startTime = time.time()

def drawCircle(app, canvas):
    canvas.create_oval(app.x0-app.r, app.y0-app.r, 
                                    app.x0+app.r, app.y0+app.r,
                                    fill = "red")

def redrawAll(app, canvas):
    drawCircle(app, canvas)

runApp(width = 650, height = 450)