from turtle import *
from random import *


def DrawStar():
    pendown()
    begin_fill()
    for side in range(5):
        forward(50)
        left(144)
    end_fill()
    penup()

for star in range(30):
    penup()
    setpos(randint(-300,300),randint(-400,400))
    DrawStar()
