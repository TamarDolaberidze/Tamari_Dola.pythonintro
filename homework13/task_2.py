from random import randrange

list_1 = [randrange(1, 101) for _ in range(10)]
list_2 = [randrange(1, 101) for _ in range(15)]
list_3 = [randrange(1, 101) for _ in range(20)]

print(list_1, list_2, list_3)

def main():
    for i in map (lambda x, y, z: x + y + z, list_1, list_2, list_3):
        print(i)

if __name__ == "__main__":
    main()