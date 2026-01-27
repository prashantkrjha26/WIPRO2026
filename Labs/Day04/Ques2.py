# Question – Parameterized Methods, Constructors & Destructors

# Topics: Parameterized Methods, Constructors & Destructors

# Create a class BankAccount that:

# 1. Uses a parameterized constructor to initialize account_number and balance
# 2. Implements methods deposit(amount) and withdraw(amount)
# 3. Uses a destructor to display a message when the object is deleted

class BankAccount:
    # Parameterized constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance {self.balance}")

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance")

    # Destructor
    def __del__(self):
        print(f"Account {self.account_number} is being deleted")


# Create object
account = BankAccount(123456, 5000)

# Perform operations
account.deposit(2000)
account.withdraw(3000)

# Delete object
del account


