input1 = input("enter a text1: ")
input2 = input("enter a text2: ") 
alphabet = "abcdefghijklmnopqrstuvwxyz" 

print(input1)
print(input2) 
found_match = True

if len(input1) == len(input2):
    for i in range (len(input1)):
        for j in range(len(input2)):
            if input1 [i] == input2[j]:
                found_match = True
                break
            else:
                found_match = False
    if found_match:
        print("YES")
    else:
        print("NO")
else:
    print("NO")