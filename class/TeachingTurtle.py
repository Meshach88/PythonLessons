from turtle import *
from random import *

shape("arrow")
speed(3)
bgcolor("blue")
color("white")

#draw a star
def drawStar(starsize,starcolor):
    pendown()
    color(starcolor)
    begin_fill()
    for count in range(5):
        forward(starsize)
        left(144)
    end_fill()
    penup()
    
def randomLocation():
    penup()
    setpos(randint(-300,300), randint(-300,300))

#Convert the lines of code below to a function (drawGalaxy) so you can tell it how many stars you want to draw. 
    
for star in range(30):
    randomLocation()
    drawStar(50,"white")






hideturtle()
done()