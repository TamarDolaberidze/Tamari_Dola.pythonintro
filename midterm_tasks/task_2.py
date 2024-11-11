n = int(input("Enter number: ")) 

if not 10 <= n <= 5432 or float(n) != int(n):
    print("Not correct number")
    exit(1)

counter = 0
for i in range(1, n):
    if i %13 == 0:
        counter += 1
        print(i)
print("Number of mulipliers", counter)