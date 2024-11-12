def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield tuple(data[i : i+chunk_size])


def main():
    dat_list_type = [5, 6, 8, 10, 15, 17, 19, 22, 20, 66]
    data_tuple_type = (10, 55, 50, 14, 15, 99, 28, 11)

    for chunk in chunk_data(dat_list_type, 3):
        print(chunk, end=" ")
    
    print()

    for chunk in chunk_data(data_tuple_type, 4):
        print(chunk, end=" ")

if __name__ == "__main__":
    main()