word = input("enter a text: ")

if len(word) %2 == 0:
    first_char = word[int(len(word)/2)-1]  #აქ int რატომ დამჭირდა ვერ ვიგებ. float როგორ იქნება len(word)/2, თუ ლუწია len(word)?
    second_char = word[int(len(word)/2)]
    print (first_char, second_char)
else:
    i = 0
    while i < 5:
       first_char = word[0:1]
       second_char = word[len(word)//2+1]
       print(first_char, second_char)
       i+=1
    
