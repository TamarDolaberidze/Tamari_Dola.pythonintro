from turtle import *

for _ in range(3):
    forward(80)
    left(120)

penup()
forward(40)
left(60)
pendown()

for _ in range(3):
    backward(100)
    left(120)

penup()
backward(100)
right(60)
forward(50)
pendown()

for _ in range(1):
    right(60)
    forward(120)
    left(60)
    backward(120)
    left(60)
    forward(120)