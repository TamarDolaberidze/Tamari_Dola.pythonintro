import random

n = int (input ("please enter a number - "))

if  0 < n < 30:
    max_num = 0
    for i in range (0, n):
        random_num = random.randint (0, 1000)
        print (random_num)
        if random_num > max_num:
                max_num = random_num
    print (max_num)
else:
    print (" enter a valid number ")

