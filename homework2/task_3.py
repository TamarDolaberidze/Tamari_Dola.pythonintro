number = int(input("enter a number - "))

if number <= 10: 
    if number % 2 == 0:
        print (2, end = " ")
    if number % 3 == 0:
        print (3, end = " ")
    if number % 5 == 0:
        print (5,  end = " ")
    if number % 7 == 0:
        print (7, end = " ")
else:
    print ("შეცდომაა")
