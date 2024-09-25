n = int(input("please enter a number: "))

if 0 < n < 50:
    for i in range (1,n+1):
        print(f"{i}", end= " - ")
        counter_j = 0
        for j in range (1,i+1):
            if i % j == 0:
                print(j, end=" ")
                counter_j += 1
            if counter_j == 3:
                break
        print ()
        
else:
    print("you entered wrong number")
    







# while divisor < n + 1 and divisor <= 3:
#     if n % divisor == 0:
#         print (f"{n} - {divisor}")
#     divisor += 1


  # 10 - 1,2,5