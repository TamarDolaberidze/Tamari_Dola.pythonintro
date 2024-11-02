def list_func(list1, list2):
    list3 = []
    list1_start_index = 0
    list2_start_index = 0
    while list1_start_index < len(list1) and list2_start_index < len(list2):
        if list1[list1_start_index] < list2[list2_start_index]:
            list3.append(list1[list1_start_index])
            list1_start_index += 1
        else:
            list3.append(list2[list2_start_index])
            list2_start_index += 1


    while list1_start_index < len(list1):
        list3.append(list1[list1_start_index])
        list1_start_index+=1

    while list2_start_index < len(list2):
        list3.append(list2[list2_start_index])
        list1_start_index+=1
    
    return list3


def main():
    list1 = [1, 3, 10]
    list2 = [0, 4, 7, 9]
    print(list_func(list1, list2))

    list3 = [2, 9, 10, 11, 14]
    list4 = [0, 3, 5, 8]
    print(list_func(list3, list4))

if __name__ == "__main__":
    main()
    