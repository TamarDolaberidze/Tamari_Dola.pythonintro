word = input("enter a text: ")
i = 0
while i < 5:
    if len(word) %2 == 0:
        first_char = word[int(len(word)/2)-1] 
        second_char = word[int(len(word)/2)]
        print (fisrst_char, second_char)
    else:
        print(word[0], word[int(len(word)/2)], word[-1])
    i += 1
        
