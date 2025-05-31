from turtle import *

shape("arrow")
speed(3)
bgcolor("blue")
color("white")

#draw a star
def drawStar():
    begin_fill()
    for count in range(5):
        forward(100)
        left(144)
    end_fill()
    

drawStar()
forward(200)
drawStar()
left(120)
forward(150)
drawStar()

#draw five stars





done()