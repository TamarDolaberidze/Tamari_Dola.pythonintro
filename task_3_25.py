from datetime import datetime

class TimestampMixing:
    def __init__(self):
        self.creation_time = datetime.now()
        self.modification_time = self.creation_time

    def get_creation_time(self):
        return f"Object creation time: {self.creation_time}"

    def get_modification_time(self):
        return f"Object modification time: {self.modification_time}"
    
    def update_modification_time(self):
        self.modification_time = datetime.now()

class File(TimestampMixing):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def update_filename(self, new_filename):
        self.filename = new_filename
        self.update_modification_time()

class User(TimestampMixing):
    def __init__(self, username):
        super().__init__()
        self.username = username
    
    def update_username(self, new_username):
        self.username = new_username
        self.update_modification_time()

def main():
    file = File("document.txt")
    print(file.get_creation_time())
    print(file.get_modification_time())

    file.update_filename("new_document.txt")
    print(file.get_modification_time())

    user = User("john_dow")
    print(user.get_creation_time())
    print(user.get_modification_time())
    
    user.update_username("meg_ryan")
    print(user.get_modification_time())

if __name__ == "__main__":
    main()