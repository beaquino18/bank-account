

from bank_account import BankAccount


class Bank:


    def displayMenu():
        print('---- Welcome to Online Banking ----')
        print(' 1. Access your account')
        print(' 2. Create an Account')
        print(' 3. Exit')


    def create_account():
        name = input("Full Name: ")
        account_type = Bank.account_type_selection()
        initial_balance = float(input("Initial Balance: "))
        
        account = BankAccount(name, initial_balance, account_type)

        print(f"\nYour account information is:\nFull Name: {name}\nAccount Type: {account_type}\nBalance: ${initial_balance}\nAccount Number: {account.account}")
        
    def account_type_selection():
        while True:
            type = input("Account Type: (Press 1 for Chequing, 2 for Savings): ")
            if type == "1":
                return "Chequing"
            elif type == "2":
                return "Saving"
            else:
                print("Invalid option. Please try again.\n")
    
    def run_application():
        while True:
            displayMenu()
            choice = input("Choose an option: ")
            
            if choice == '1':
              username = input("Enter your username: ")
              password = input("Enter your password: ")
              user = login(username, password)
              if user:
                  account(user)
            
            elif choice == '2':
              print("Account creation is not available right now")
            elif choice == '3':
              print("Exiting... Have a nice day!")
              break
            else:
              print("Invalid option. Please try again.")


Bank.create_account()
