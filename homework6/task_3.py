n = int(input("enter a number: "))

if 0 <= n < 10000:
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    sum = 0
    k = 0
    while n>0:
        if n>=1000:
            n = n - 1000
            count += 1
            sum += 1
        elif n>=100:
            n = n - 100
            count1 += 1
            sum += 1
        elif n>=10:
            n = n - 10
            count2 += 1
            sum += 1
        elif n>0:
            n = n - 1
            count3 += 1
            sum += 1

reversed_num = ""

if count3 > 0:
    reversed_num += str(count3)
if count2 > 0:
    reversed_num += str(count2)
if count1 > 0:
    reversed_num += str(count1)
if count > 0:
    reversed_num += str(count)    

print(f"reversed number is: {reversed_num}")  
print(f"sum of digits: {sum}")



