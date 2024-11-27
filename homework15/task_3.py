friend_list = {}

while True:
    connection = input("Enter a text: ").strip()

    if connection == "FINISH":
        break

    if "-" in connection:
        person1, person2 = map(str.strip, connection.split("-"))

        if person1 not in friend_list:
            friend_list[person1] = set()
        if person2 not in friend_list:
            friend_list[person2] = set()

        friend_list[person1].add(person2)
        friend_list[person2].add(person1)

print("Output:")
for person, friends in friend_list.items():
    print(f"{person} - {', '.join(sorted(friends))}")
