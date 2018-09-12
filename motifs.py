import turtle
import random
cols=['blue', 'green', 'red', 'yellow']
turtle.speed(0)
turtle.pensize(8)
for a in range (100):
    max=random.randint(0,200)
    min=random.randint(-200,0)
    x=random.randint(min,max)
    y=random.randint(min,max)
    turtle.color(random.choice(cols))
    turtle.goto(x,y)
