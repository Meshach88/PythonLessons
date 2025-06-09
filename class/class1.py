from turtle import *
from random import *

shape("turtle")
color('green')
bgcolor('midnight blue')
speed(5)

def makeStar(starSize,starColor):
    pendown()
    color(starColor)
    begin_fill()
    for side in range(5):
        forward(starSize)
        left(144)
    end_fill()
    penup()

def randomLocation():
    penup()
    setpos(randint(-300,300),randint(-300,300))

def drawGalaxy(numberOfStars):
    colors = ['pink','yellow','orange','green']
    for star in range(numberOfStars):
        randomLocation()
        makeStar(randint(5,30), choice(colors))

drawGalaxy(30)


hideturtle()
done()
