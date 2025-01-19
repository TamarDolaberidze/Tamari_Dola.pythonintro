import json
import getpass

admin_auth = "adminPsw.json" #ადმინის პასვორდისა და იუზერნეიმის ფაილი

class AdminAuth:
    #მოწმდება მომხმარებლის მიერ შეყვანილი მონაცემების სისწორე
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print("\n🔐 Admin Login. You have three attempts to log in.")
        
        attempts = 0 #შესვლის ცდების ინიციალიზაცია

        #სამი ცდა შესვლისთვის
        while attempts < 3:
            input_username = input("Enter username: ")
            input_password = getpass.getpass("Enter password: ")

            if input_username == self.username and input_password == self.password:
                print("✅ Access granted. Welcome, Admin!")
                return True
            else:
                attempts += 1
                remaining_attempts = 3 - attempts
                if remaining_attempts > 0:
                    print(f"❌ Invalid credentials. You have {remaining_attempts} attempt(s) left.")
                else:
                    print("❌ Too many failed attempts. Access denied.")
                    return False
            
def load_admin_credentials(file_path):
    #კითხულობს JSON ფაილს, საიდანაც იღებს username და password
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data["username"], data["password"]
    except FileNotFoundError: 
        print("❌ Error: Admin credentials file not found.")
        return None, None
    




