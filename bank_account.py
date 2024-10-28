import random

class BankAccount:
    def __init__(self, full_name, balance, account_type):
        self.name = full_name
        self.account = self.random_account_number()
        self.balance = balance
        self.type = account_type

    def random_account_number(self):
        return random.randint(10000000, 99999999)
    
    def mask_account_number(self):
        masked_number = f"****{str(self.account)[-4:]}"
        return masked_number

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} | New balance: ${self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance > amount:
            print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")
        else:
            self.balance += 10
            print("Insufficient funds. Overdraft fee of $10 charged to your account.")
    
    # Prints total balance
    def get_balance(self):
        print(f"Balance: ${self.balance}")

    # Add interest method with annual rate of 1% or 0.00083 per month
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    # Print method
    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account}\nAccount Type: {self.type}\nBalance: ${self.balance}")


# # Bank account examples
# bank_account1 = BankAccount("Ron", 50000, "chequing")
# bank_account1.print_statement()

