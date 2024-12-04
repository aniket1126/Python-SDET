class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount} New balance: ${self.balance}")
            else:
                print("Insufficient funds")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance}")


account = BankAccount("aniket", 500)


account.deposit(200)

account.withdraw(100)
account.check_balance()
