n = int(input("enter a number: "))

if 0 <= n < 20:
    x,y = 0,1
    i = 0
    while i <= n:
        if i >= 2:
            summ = x+y
            x,y =y,summ
        elif i == 0:
            summ = x 
        elif i == 1:
            summ = y
        print(summ, end=" ")
        i += 1
            

        

















else:
    print("enter a valid number")
