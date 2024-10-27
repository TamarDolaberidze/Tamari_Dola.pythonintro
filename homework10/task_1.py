def x(y):
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

vowels = "aeiouAEIOU"
text = input("ener a text: ")
result = x(text)
print(result)