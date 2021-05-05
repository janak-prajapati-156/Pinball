from cmu_112_graphics import *
import ball
#sidebar

def drawInstructions(app, canvas):
    playWidth = app.width*4.5/7
    text = ["Press SPACEBAR to start", "Press 'r' to restart", 
            "Use a BLUE object to move", 
            "the RIGHT flipper",
            "Use a RED object to move",
            "the LEFT flipper"]
    for i in range(len(text)):
        canvas.create_text((playWidth+app.width)/2, (app.height/8)+(20*i),
                            text = text[i], font = 'Helvetica 16')

def drawScore(app, canvas):
    playWidth = app.width*4.5/7
    canvas.create_text((playWidth+app.width)/2, app.height/2, 
                        text = f"Score : {app.score}", font = 'Helvetica 16')