from cmu_112_graphics import *
import ball
#sidebar

def drawInstructions(app, canvas):
    playWidth = app.width*4.5/7
    text = ["Press RETURN to enter username", 
            "Press SPACEBAR to start", "Press 'r' to restart", 
            "Press 'q' to quit game",
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

def keepScores(app):
    # app.scorelist = []
    with open('score.txt', 'r') as file:
        for line in file:
            if not line[-1].isnumeric():
                line = line[:-1]
            app.scorelist.append(line)
    newScores = getScores(app.scorelist)

    with open('score.txt', 'w') as file:
        for num in newScores:
            num = str(num)
            for line in app.scorelist:
                if num == line.split(' ')[-1]:
                    file.write(f'{line}\n')

    with open('score.txt', 'r') as file:
        app.scorelist = []
        for line in file:
            if not line[-1].isnumeric():
                line = line[:-1]
            app.scorelist.append(line)

def highscores(app, canvas):
    playWidth = app.width*4.5/7
    for i in range(5):
        if i>=len(app.scorelist):
            break
        canvas.create_text((playWidth+app.width)/2, (app.height*3/4)+(20*i),
                            text = app.scorelist[i], font = 'Helvetica 16')
    
def getScores(L):
    result = []
    newLine = None
    for line in L:
        newLine = line
        result.append(int(newLine.split(' ')[-1]))
    result.sort()
    result.reverse()
    return result
