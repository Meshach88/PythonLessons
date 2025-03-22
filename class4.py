from turtle import *

speed(5)

#loop
sides = 4
angle = 360/sides

for side in range(sides):
    forward(100)
    left(angle)
    

hideturtle()
done()