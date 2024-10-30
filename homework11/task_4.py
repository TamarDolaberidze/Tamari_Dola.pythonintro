import timeit

from task_2_1 import gcd_iter
from task_2_2 import gcd_rec

def main():
    result = timeit.timeit(lambda: gcd_rec(400, 1000), number = 1000)
    print("time passed: ", result)

    result = timeit.timeit(lambda: gcd_iter(400, 1000), number = 1000)
    print("time passed iter: ", result)


if __name__ == "__main__":
    main()

