def gcd_iter(a,b):
    if b == 0:
        return a
    else:
        m = min(a, b)
        while m > 0:
            if a % m == 0 and b % m == 0:
                return m
            m -= 1
        return abs(m)

def main():
    a = int(input("enter a number: "))
    if a <= 0:
        exit(1)
    b = int(input("enter a number: "))
    if b > 10000:
        exit(1)
    result = gcd_iter(a, b)
    print(f"the great common divisor of {a} and {b} is {result}")

if __name__ == "__main__":
    main()        