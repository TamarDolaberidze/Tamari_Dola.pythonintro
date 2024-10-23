import turtle
from random import uniform
from math import sqrt

n = int(input("enter a number: "))
if n<1:
    exit(1)
    
def draw_ab(a, b, color):
    turtle.penup()
    turtle.goto(a * 100, b * 100)
    turtle.pendown()
    turtle.dot(5, color)



def num_pairs(n):
    for i in range(n):
        a = uniform(0, 1)
        b = uniform(0, 1)
        if sqrt(a ** 2 + b ** 2) <= 1:
            draw_ab(a, b, "red")
        else:
            draw_ab(a, b, "green")
    turtle.done()

num_pairs(n)

