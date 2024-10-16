action = input("enter action e/d: ")

if action != "e" and action != "d":
    print("not correct action")
    exit(-1)

text = input("enter text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
original = "qwertyuiopasdfghjklzxcvbnm"
shifted = "wertyuiopasdfghjklzxcvbnmq"

text_new = ""

for z in text:
    if z.isupper() or z not in alphabet:
        text_new += z
        print(text_new)
    elif z == "p" or z == "l" or z == "m":
        text_new += z
        print(text_new)
    else:
        text_new += z.translate(str.maketrans(original, shifted))
        print(text_new)
    

text_new_1 = text_new.replace("p", "q")
text_new_2 = text_new_1.replace("l", "a")
text_new_3 = text_new_2.replace("m", "z")

print(text_new_3)