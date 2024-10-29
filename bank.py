import os
import sys
from bank_account import BankAccount

# STRETCH CHALLENGE
class Bank:
    # A function that reads the data.txt
    def load_data():
      with open('data.txt', 'r') as f:
        data_list = [line.strip().split(',') for line in f.readlines()]
      return data_list
    
    # A function that saves data and stores in data.txt
    def save_data(username, password, name, account_type, balance, account_number):
       account_data = f"{username},{password},{name},{account_type},{balance},{account_number}"

       with open('data.txt', 'a') as f:
          f.write(account_data)
      
    def display_menu():
      print('----- WELCOME TO ONLINE BANKING -----')
      print(' 1. Access your account')
      print(' 2. Create an Account')
      print(' 3. Exit\n')
    
    # Displays account menu option when user logins
    def account_menu():
      print('----- ACCOUNT INFORMATION -----')
      print(' 1. Deposit')
      print(' 2. Withdrawal')
      print(' 3. Log Out')

    # Option to create account - STRETCH CHALLENGE
    def create_account():
      username = input("Username: ")
      password = input("Password: ")
      name = input("Full Name: ")
      account_type = Bank.account_type_selection()
      initial_balance = float(input("Initial Balance: "))
        
      account = BankAccount(name, initial_balance, account_type)

      Bank.save_data(username, password, name, account_type, initial_balance, account.account)

      print("\nYour account information is:\n")
      print("================================\n")
      print(f"Username: {username}\nFull Name: {name}\nAccount Type: {account_type}\nBalance: ${initial_balance}\nAccount Number: {account.account}")
      print("\n================================")

    def account_type_selection():
      while True:
          type = input("Account Type: (Press 1 for Chequing, 2 for Savings): ")
          if type == "1":
            return "Chequing"
          elif type == "2":
            return "Saving"
          else:
            print("Invalid option. Please try again.\n")

    def deposit():
      while True:
        print("----- DEPOSIT -----")
        print("1. Deposit to an account\n2. Return to main menu\n")
        choice = input("Choose an option: ")
        
        Bank.clear_screen()
        
        if choice == "1":
          Bank.deposit_to_account()
        elif choice == "2":
          return
        else:
          print("Invalid option. Please try again.\n")
    
    def deposit_to_account():
      while True:
        account_number = input("Enter the account number: ")
        data_list = Bank.load_data()
        found = False
        
        for i, user in enumerate(data_list):
          if user[5] == account_number:
            found = True
            user_data = {
              "Username": user[0],
              "Full Name": user[2],
							"Account Type": user[3],
							"Balance": float(user[4]),
							"Account Number": user[5]
						}
            print("\n================================")
            print(f"Account information:\nName: {user[2]}\nAccount Type: {user[3]}\nAccount Number: {user[5]}")
            print("================================\n")
            
            while True:
              try:
                deposit_amount = float(input(f"How much would you to deposit to {user[2]}'s account? "))
                if deposit_amount <= 0:
                  print("\n================================")
                  print("Deposit amount must be greater than zero. Please try again.")
                  print("================================")
                  continue
                
                user_data["Balance"] += deposit_amount
                data_list[i][4] = str(user_data["Balance"])
                
                # Save updated data back to data.txt
                with open('data.txt', 'w') as f:
                  for account in data_list:
                    f.write(','.join(account) + '\n')
                    
                print("\n================================")
                print(f"Successfully deposited ${deposit_amount} to {user[2]}'s account")
                print("================================\n")
                
                return
              
              except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
        
        if not found:
          print("\n================================")
          print("Account number not found!! Please try again.")
          print("================================\n")
           
             
    def withdraw(user):
      while True:
        print("----- WITHDRAW -----")
        print("1. Withdraw from your account\n2. Return to main menu\n")
        choice = input("Choose an option: ")
        
        Bank.clear_screen()
        
        if choice == "1":
          Bank.withdraw_own_account(user)
        elif choice == "2":
          return
        else:
          print("Invalid option. Please try again.\n")
    
    def withdraw_own_account(user):
      balance = float(user["Balance"])
      print(f"Account Balance: ${balance}")
      
      while True:
        try:
          withdraw_amount = float(input("How much would you like to withdraw from your account? "))
          
          if withdraw_amount <= 0:
            print("\n================================")
            print("Withdraw amount must be greater than zero. Please try again.")
            print("================================\n")
            return
          
          if withdraw_amount > balance:
            print("\n================================")
            print("Insufficient funds. Overdraft fee of $10 charged to your account.")
            print("================================\n")
            new_balance = balance - (withdraw_amount + 10) #Charge overdraft fees
          else:
            new_balance = balance - withdraw_amount
            
          user["Balance"] = new_balance
          
          #Load data to update file
          data_list = Bank.load_data()
          for i, entry in enumerate(data_list):
            if entry[0] == user["Username"]:
              entry[4] = str(new_balance)
              break
          
          # Save updated data back to data.txt
          with open('data.txt', 'w') as f:
            for account in data_list:
              f.write(','.join(account) + '\n')
              
          print("\n================================")
          print(f"Successfully withdrew ${withdraw_amount}.\nNew Balance: ${new_balance}")
          print("================================\n")
          return
        
        except ValueError:
          print("Invalid amount. Please enter a valid number.")
          continue
      
      
    
    def transfer():
       #TODO
       return
    
    def statement():
       #TODO
       return
    


    # Allows user to login with the correct username and password
    def login(username, password):
      data_list = Bank.load_data()

      for user in data_list:
        if user[0] == username and user[1] == password:
            user_data = {
                "Username": username,
                "Full Name": user[2],
                "Account Type": user[3],
                "Balance": (user[4]),
                "Account Number": user[5]
            }
            print("================================")
            print(f"Welcome {user[2]}!")
            print(f"Account Number: {user[5]}\nAccount Type: {user[3]}\nBalance: ${user[4]}")
            print("================================\n")
            return user_data
        
      print("\n================================\n")  
      print("Username and password not found!! Please try again.\n")
      print("\n================================\n")
      return None

    # Allows user to make actions when logged in to their account
    def account(user):
      while True:
        Bank.account_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
          Bank.clear_screen()
          Bank.deposit() 
        elif choice == '2':
          Bank.clear_screen()
          Bank.withdraw(user)
        elif choice == '3':
          print("Logging off...Goodbye!\n")
          sys.exit()
        else:
          print("Invalid option. Please try again.\n")   
    
    def clear_screen():
       os.system('clear')

    # Runs the application
    def run_application():
      while True:
          Bank.display_menu()
          choice = input("Choose an option: ")
          Bank.clear_screen()
          
          if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            Bank.clear_screen()  
            user = Bank.login(username, password)
            if user:
                Bank.account(user)
          elif choice == '2':
            Bank.create_account()
          elif choice == '3':
            print("Exiting... Have a nice day!")
            break
          else:
            print("Invalid option. Please try again.")




Bank.run_application()
