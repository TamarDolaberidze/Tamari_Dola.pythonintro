def gcd_rec(x, y):
    if y == 0:
        return abs(x)
    return gcd_rec(y, x % y)

def main():
    a = int(input("enter a number: "))
    if a <= 0:
        exit(1)
    b = int(input("enter a number: "))
    if b > 10000:
        exit(1)

    x = min(a, b)
    y = max(a, b)

    result = gcd_rec(x, y)
    print(f"the great common divisor of {a} and {b} is {result}")



if __name__ == "__main__":
    main() 