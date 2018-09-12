import turtle
turtle.pensize(5)

def drawUp():
    turtle.seth(90)
    turtle.fd(20)
def drawDown():
    turtle.seth(270)
    turtle.fd(20)
def drawLeft():
    turtle.seth(180)
    turtle.fd(20)
def drawRight():
    turtle.seth(0)
    turtle.fd(20)
def setRed():
    turtle.color('red')
def setGreen():
    turtle.color('green')

turtle.onkey(drawUp,'Up')
turtle.onkey(drawDown,'Down')
turtle.onkey(drawLeft,'Left')
turtle.onkey(drawRight,'Right')
turtle.onkey(setRed,'r')
turtle.onkey(setGreen,'g')

turtle.listen()
