n = int(input("enter a number: "))
if 0 < n < 10:
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print (j, end=" ")
            j+=1
        print ()
        i+=1

    k = n-1
    while 0 < k <= n:
        l = 1
        while l <= k:
            print (l, end=" ")
            l+=1
        print()
        k-=1
else:
    print ("not correct")
    