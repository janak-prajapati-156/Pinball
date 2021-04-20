import numpy as np, cv2
from cmu_112_graphics import *

class pinball(object):
    def __init__(self):
        self.radius = "janak"

    def appStarted(app, self):
        app.bool = False

    def redrawAll(app, canvas, self):
        canvas.create_text(app.width/2, app.height/2, text = str(self.radius))

    runApp(width=650, height=550)