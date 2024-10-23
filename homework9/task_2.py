n = int(input("enter a number: "))
if n<1:
    exit(1)

from random import uniform
from math import sqrt

counter = 0
for i in range(n):
    a = uniform(0, 1)
    b = uniform(0, 1)
    if sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1
print(4 * counter / n)