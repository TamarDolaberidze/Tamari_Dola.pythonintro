import json 

#ფაილი მომხმარებელთა მონაცემების შესანახად
user_data_file = "users.json"

class User:
    def __init__(self, user_id, username, password, balance):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.balance = balance

#კლასი მომხმარებლების რეგისტრაციისთვის
class UserManager:
    def __init__(self):
    # Load existing users from the file or initialize an empty list
        self.users = self.load_users()
        self.next_id = self.get_next_id()


    #კითხულობს ფაილს და მოაქვს იუზერები, თუ არ არსებობს ფაილი, ქმნის []
    def load_users(self):
        try:
            with open(user_data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        

    def save_users(self):
        #მომხმარებელს წერს json ფაილში 4 სფეისით (indent)
        with open(user_data_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def get_next_id(self):
        #ინსტანსის მიხედვით ბოლო მომხმარებლის აიდი +1, თუ ჩანაწერები არ არის ვანიჭებ id = 1
        if self.users:
            return self.users[-1]["user_id"] + 1
        return 1

    def register_user(self, username, password, balance):
        #რეგისტრაცია.
        
        #ამოწმებს იუზერნეიმის უნიკალურობას
        while any(user['username'] == username for user in self.users):
            print(f"❌ The username '{username}' is already taken. Please choose a different one.")
            username = input("Enter a new username: ")
        
        user = User(self.next_id, username, password, balance)
        self.users.append({
            "user_id": user.user_id,
            "username": user.username,
            "password": user.password,
            "balance" : user.balance
        })
        self.next_id += 1
        self.save_users()
        print(f"✅ User '{username}' registered with ID: {user.user_id}")
    


