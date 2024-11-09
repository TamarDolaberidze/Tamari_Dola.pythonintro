def x(y):
    if y<=1 or y!=2 and y%2 ==0:
        return "not prime number"
    elif y % 2 != 0:
        for i in range(2, y):
            if y %i == 0:
                return "not prime number"
        return "prime number"
    elif y == 2:
        return "prime number"
                           

number = int(input("enter a number: "))
result = x(number)
print(result)