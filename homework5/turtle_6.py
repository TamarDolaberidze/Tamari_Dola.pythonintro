from turtle import *
from time import *

text = 'Python'

pencolor('green')

for char in text:
    write(char, align='center', font=('Comic Sans MS', 20, 'normal'))
    forward(20)
    sleep(0.5)

sleep(3)