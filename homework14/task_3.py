def fib_numbers(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b

def main():
    print(list(fib_numbers(5)))
    print(list(fib_numbers(15)))

if __name__ == "__main__":
    main()