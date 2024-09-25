
from math import ceil

n = int(input("enter a number: "))
if 0 < n < 50:
    for i in range(1, n+1):
        if i==1:
            print ((" "*(n-i-1)), "/*\\")
        elif i>1 and i< n:
            print(" "*(n-i),"/","*"*(2*i-1),"\\",sep="")
        elif i <= n:
            print(" "*ceil(n-2),"| |")
    

else:
    print("enter a valid number")
