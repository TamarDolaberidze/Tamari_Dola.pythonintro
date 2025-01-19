import json

User_auth = "users.json"


class UserAuth:
    #მოწმდება მომხმარებლის მიერ შეყვანილი მონაცემების სისწორე
    def __init__(self, users):
        self.users = users
        self.user_id = None #ვაინიცილიზებთ None-ზე user_id-ის

    def login(self):
        print("\n🔐 User Login. You have three attempts to log in.")
        
        attempts = 0 #შესვლის ცდების ინიციალიზაცია

        while attempts < 3: #სამი ცდა შესვლისთვის
            input_username = input("Enter username: ")
            input_password = input("Enter password: ")

            #თითოეულ იუზერზე იტერაცია ლისთში, რათა match იპოვოს
            for user in self.users:
                if user["username"] == input_username and user["password"] == input_password:
                    self.user_id = user["user_id"] #იუზერის აიდის დაყენება კონკრეტული იუზერისთვის
                    print(f"✅ Access granted. Welcome, {input_username}!")
                    return True

            #თუ match ვერ იპოვა პროგრამამ   
            attempts += 1
            remaining_attempts = 3 - attempts
            if remaining_attempts > 0:
                print(f"❌ Invalid credentials. You have {remaining_attempts} attempt(s) left.")

        #თუ შესვლის სამივე ცდა ჩავარდა
        print("❌ Too many failed attempts. Access denied.")
        return False

    def get_user_id(self):
        return self.user_id # იუზერის აიდის დაბრუნება, სხვა კლასებიდანაც რომ მივწვდეთ, თუ გვინდა
    
def load_user_credentials(user_file_path):
    #კითხულობს JSON ფაილს, საიდანაც იღებს username და password
    try:
        with open(user_file_path, 'r') as file:
            data = json.load(file)
            for user in data:
                user["balance"] = float(user["balance"])
            return data
    except FileNotFoundError: 
        print("❌ Error: Users credentials file not found.")
        return []

def save_user_credentials(user_file_path, users):
    # თუ რამე დააფდეითდება იუზერში, რომ შეინახოს
    try:
        with open(user_file_path, 'w') as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"❌ Error saving user credentials: {e}")

