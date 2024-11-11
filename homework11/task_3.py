from task_2_2 import gcd_rec

def lcm(a, b):
    return abs((a * b) / gcd_rec(a, b))



def main():
    a = int(input("enter a number: "))
    if a <= 0:
        exit(1)
    b = int(input("enter a number: "))
    if b > 10000 or b == 0:
        exit(1)

    result = int(lcm(a, b))
    print(f"the least common multiple of {a} and {b} is {result}")



if __name__ == "__main__":
    main() 