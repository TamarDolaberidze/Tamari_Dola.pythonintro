s = input("enter a word: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

new_s = s.strip()
new_s_1 = new_s.replace(" ", "")
new_s_2 = new_s_1.lower()

for char in new_s_2:
    if char not in alphabet:
        new_s_2 = new_s_2.replace(char, "")

print(new_s_2)

char_backwards = -1
is_palindrome = True
for i in range(len(new_s_2)):
    if new_s_2[i] == new_s_2[char_backwards]:
        is_palindrome = True
        char_backwards-=1
    else:
        is_palindrome = False
        break
if is_palindrome:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")


   
       

    
       
        

