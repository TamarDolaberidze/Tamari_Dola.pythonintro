import random
lst = list()
while len(lst) < 50:
    lst.append(random.randrange(1, 30))
print(lst)

new_list = []
for i in lst:
    for j in range(i):
        new_list.append(i)
print(f"List length is: {len(new_list)}")
print(f"New list is: {new_list}")