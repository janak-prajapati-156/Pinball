from cmu_112_graphics import *

def initialisePoints(app):
    playWidth = app.width*4.5/7
    app.objectDict = {}
    app.objectDict['sectionLine'] = [[(playWidth, 0), 
                                    (playWidth, app.height)]]
    app.objectDict['drawEdge'] = [ 
        [ (0, app.height*7/8), (playWidth/3, app.height*7.5/8), 
            (playWidth/3, app.height), (0, app.height)], 

        [(playWidth*2/3, app.height*7.5/8), (playWidth, app.height*7/8), 
            (playWidth, app.height), (playWidth*2/3, app.height)], 

        [(0, 0), (playWidth/4, 0), 
            (playWidth/4, app.height/10), (0, app.height/5)], 
        
        [(playWidth/4, 0), (playWidth*3/4, 0), 
            (playWidth*3/4, app.height/10), (playWidth/4, app.height/10)],
        
        [(playWidth*3/4, 0), (playWidth, 0), 
            (playWidth, app.height/5), (playWidth*2/3, app.height/10)]
    ]  
    app.objectDict['flipper'] = [
        [(playWidth*1.75/9, app.height*7.08/8), 
            (playWidth*2.25/5, app.height*7.5/8), (playWidth*2.25/5, app.height*7.68/8),
            (playWidth*1.75/9, app.height*7.26/8)],

        [(playWidth*7.25/9, app.height*7.08/8), 
            (playWidth*2.75/5, app.height*7.5/8), (playWidth*2.75/5, app.height*7.68/8), 
            (playWidth*7.25/9, app.height*7.26/8)]
    ]
    app.objectDict['triangularBox'] = [
        [(playWidth/5, app.height*3/5), (playWidth/3, app.height*3.75/5),
        (playWidth/5, app.height*3.5/5)],

        [(playWidth*4/5, app.height*3/5), (playWidth*2/3, app.height*3.75/5),
        (playWidth*4/5, app.height*3.5/5)]
    ]
    width1 = playWidth/10
    width2 = playWidth/5
    height1 = app.height/10
    app.objectDict['rhombus'] = [

        [(playWidth/2, app.height/4), (playWidth*21/40, app.height*11/40),
        (playWidth/2, app.height*12/40), (playWidth*19/40, app.height*11/40)],
        
        [(playWidth/2+width2, app.height/4), (playWidth*21/40 + width2, app.height*11/40),
        (playWidth/2 + width2, app.height*12/40), (playWidth*19/40 + width2, app.height*11/40)],

        [(playWidth/2-width2, app.height/4), (playWidth*21/40 - width2, app.height*11/40),
        (playWidth/2 - width2, app.height*12/40), (playWidth*19/40 - width2, app.height*11/40)],

        [(playWidth/2-width1, app.height/4 - height1), (playWidth*21/40 - width1, app.height*11/40 - height1),
        (playWidth/2 - width1, app.height*12/40 - height1), (playWidth*19/40 - width1, app.height*11/40 - height1)],

        [(playWidth/2 + width1, app.height/4 - height1), (playWidth*21/40 + width1, app.height*11/40 - height1),
        (playWidth/2 + width1, app.height*12/40 - height1), (playWidth*19/40 + width1, app.height*11/40 - height1)]
    ]

    app.objectDict['parallelogram'] = [
        [(0, app.height/2.25), (playWidth/4, app.height/2.25 - app.height/10), 
        (playWidth/4, app.height/2.25), (0, app.height/2.25 + app.height/10)],

        [(playWidth, app.height/2.25), (playWidth*3/4, app.height/2.25 + app.height/10), 
        (playWidth*3/4, app.height/2.25), (playWidth, app.height/2.25 - app.height/10)]
    ]
    
def flipper(app, canvas):
    for objectDraw in app.objectDict['flipper']:
        canvas.create_polygon(objectDraw, fill = 'brown')

def parallelogram(app, canvas):
    for objectDraw in app.objectDict['parallelogram']:
        canvas.create_polygon(objectDraw, fill = 'green')

def drawEdge(app, canvas):
    for objectDraw in app.objectDict['drawEdge']:
        canvas.create_polygon(objectDraw, fill = 'blue')

def sectionLine(app, canvas):
    canvas.create_line(app.objectDict['sectionLine'])

def triangularBox(app, canvas):
    for objectDraw in app.objectDict['triangularBox']:
        canvas.create_polygon(objectDraw, fill = 'green')

def rhombus(app, canvas):
    for objectDraw in app.objectDict['rhombus']:
        canvas.create_polygon(objectDraw, fill = 'green')
