from turtle import *

shape("arrow")
color('red')
speed(3)
pensize(3)

sides = 8
angle = 360/sides

for side in range(sides):
    forward (100)
    left(angle)


hideturtle()
done()
