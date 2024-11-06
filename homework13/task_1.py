from random import randrange

list_1 = [randrange(0, 1000000000) for _ in range(0, 100)]

print(list_1)

def main():
    ascending_list = list(map(lambda x: x, sorted(list_1)))
    descending_list = list(map(lambda x: x, sorted(list_1, reverse=True)))
    print("ascending sorted:", ascending_list)
    print("descending sorted:", descending_list)

    string_list = list(map(lambda x: str(x), ascending_list))
    print(string_list)
    
    max_len_element = max(string_list, key=len)
    min_len_element = min(string_list, key=len)
    
    print(f"Max length element is: {max_len_element}, Min length element is: {min_len_element}")


if __name__ == "__main__":
    main()