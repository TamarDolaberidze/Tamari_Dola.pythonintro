n = int (input ("please enter a number: "))

if 0 < n < 1000: 
    for i in range (1, n+1):
        if n %i == 0:
            print (i, end= " ")
