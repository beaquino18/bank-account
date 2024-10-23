import random

class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} | New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance > amount:
            print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")
        else:
            self.balance += 10
            print("Insufficient funds. Overdraft fee of $10 charged to your account.")
    
    def get_balance(self):
        print(f"Balance: ${self.balance}")

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        print(f"{self.name}\nAccount No.: \nBalance: ${self.balance}")
