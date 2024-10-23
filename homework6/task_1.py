from random import randrange

x = randrange(0, 100)
print(x)

attempt_num = 0
while attempt_num < 10:
    y = int(input("enter a number: "))
    attempt_num+=1

    if x == y:
        print("you are winner")
        break
    elif y>x:
        print("high")
    elif y<x:
        print("low")

if attempt_num == 10:
    print("computer is winner")

