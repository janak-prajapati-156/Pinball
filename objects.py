from cmu_112_graphics import *

def initialisePoints(app):
    playWidth = app.width*4.5/7
    app.objectDict = {}
    app.objectDict[sectionLine] = [[(playWidth, 0), 
                                    (playWidth, app.height)]]
    app.objectDict[drawEdge] = [ 

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
    
def drawEdge(app, canvas):
    for objectDraw in app.objectDict[drawEdge]:
        canvas.create_polygon(objectDraw, fill = 'blue')

def sectionLine(app, canvas):
    canvas.create_line(app.objectDict[sectionLine])

def triangularBox(app, canvas):
    pass
