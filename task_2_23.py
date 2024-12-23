class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, v):
        self._balance = v

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough money")
        else:
            self._balance -= amount
    
    def get_balance(self):
        return self._balance

def main():
    account = BankAccount(100)

    account.deposit(50)
    account.withdraw(30)
    account.withdraw(200)

    print(f"Final balance: {account.get_balance()}")

if __name__ == "__main__":
    main()