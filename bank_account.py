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
        return amount

    # Withdraw method
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance > amount:
            print(f"Amount withdrawn: ${amount} | New balance: ${self.balance}")
            return amount
        else:
            self.balance += 10
            print("Insufficient funds. Overdraft fee of $10 charged to your account.")
            return amount
    
    # Prints total balance
    def get_balance(self):
        print(f"Balance: ${self.balance}")

    # Add interest method with annual rate of 1% or 0.00083 per month
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    # Print method
    def print_statement(self):
        print(f"\n{self.name}\nAccount No.: {self.mask_account_number()}\nAccount Type: {self.type}\nBalance: ${self.balance}")


def run_application():
    # Instantiate 3 Bank Accounts
    bank_account1 = BankAccount("Ron Weasley", 500, "Chequing")
    bank_account2 = BankAccount("Hermione Granger", 1000, "Savings")
    bank_account3 = BankAccount("Harry Potter", 2000, "Savings")

    # Print Statements
    bank_account1.print_statement()
    bank_account2.print_statement()
    bank_account3.print_statement()
    print("-------------------------------------")

    #Deposit amount 
    amount_deposit = bank_account1.deposit(50)
    print(f"Successfully deposited ${amount_deposit} to {bank_account1.name}'s account")

    # Print statement
    bank_account1.print_statement()

    #Add interest
    interest_amount = bank_account1.add_interest()
    print(f"{bank_account1.name}'s bank account earn interest of {interest_amount}")

    # Print statement
    bank_account1.print_statement()

    # Withdraw amount
    withdraw_amount = bank_account1.withdraw(700)
    print(f"Successfully withdrew ${withdraw_amount} to {bank_account1.name}'s account")

    # Print statement
    bank_account1.print_statement()
    



