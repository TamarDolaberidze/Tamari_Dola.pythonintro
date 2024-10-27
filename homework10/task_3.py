def x(y):
    start = 1
    for i in range(1, y+1):
        start *= i
    return start

number = int(input("enter a number: "))
result = x(number)
print(result)