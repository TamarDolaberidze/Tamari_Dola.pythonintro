n = int(input("enter a number: "))
if n<1:
    exit(1)

x = 0
for i in range(1, n+1):
    if i %2 == 0:
        x -= 4*(1/(2*i-1))
    else:
        x += 4*(1/(2*i-1))
print(x)