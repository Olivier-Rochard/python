import turtle
import random

a = turtle.Turtle()
a.color('red')
b = turtle.Turtle()
b.color('blue')
c = turtle.Turtle()
c.color('green')
turtles = [a,b,c]
for item in turtles:
    item.penup()
    item.shape('turtle')
    item.shapesize(4,4)
a.goto(-300,-100)
b.goto(-300,0)
c.goto(-300,100)
for race in range(100):
    for item in turtles:
        item.fd(random.randint(0,12))
