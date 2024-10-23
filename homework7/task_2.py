text = input("enter a text: ")

vowels = "aeiou"
new_word = ""

for i in range(len(text)):
    if text[i] not in vowels:
        new_word+= text[i]

print(new_word)
