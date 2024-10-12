n = int(input("enter a number: "))
if 0 < n <= 1000:
    num=n
    while num>0:
        print(int(num), end=" ")
        if num %2 == 0:
            num = num/2
            print("->", end=" ")
        elif num == 1:
            num = 1
            break
        elif num %2 != 0:
            num = (num*3)+1
            print(" -> ", end=" ")
else:
    print("not correct")