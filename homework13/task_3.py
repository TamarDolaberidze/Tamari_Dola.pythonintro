words_list = ["cat", "belt", "dog", "air", "darkness", "light"]

def main():
    new_words_list = list(map(lambda x: x.upper() if len(x) <= 3 else x.replace(x, ""), words_list))
    print(new_words_list)

    filtered_new_words_list = [x for x in new_words_list if x != '']
    print(filtered_new_words_list)



if __name__ == "__main__":
    main()