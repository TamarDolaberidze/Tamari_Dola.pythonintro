import random
lst = list()
while len(lst) < 50:
    lst.append(random.randrange(1, 30))
print(lst)

new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)

print(f"List length is: {len(new_list)}")
print(f"New list is: {new_list}")