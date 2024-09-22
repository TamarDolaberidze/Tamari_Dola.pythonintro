n = int (input ("please enter a number: "))
 
a, b = 0, 1

if 0 <= n < 20: 
    if n == 0:
        print (a)
    elif n == 1:
        print (b)
    else: 
        for i in range(2, n+1):
            a, b = b, a+b
        print (b)
    
        
        
        
