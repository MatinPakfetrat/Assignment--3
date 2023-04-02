"""Contains the class program."""

from Bank import *

class Program:
    """Implements all the interaction between the user and the Bank."""

    def run(self):
        """Runs the program."""
        self.b = Bank()
        self.showMainMenu()

    def showMainMenu(self):
        """Loops to display the main menu options."""
        while True:
            print("1. Open Account\n2. Select Account\n3. Exit")
            choice = input("Please enter an option: ").title()

            if choice == "1" or choice == "Open Account":  #Opens an account.
                try:
                    num = int(input("Please enter the account number: "))
                    interest = float(input("Please enter the rate of interest: "))
                    balance = float(input("Please enter the current balance: "))
                except ValueError:
                    print("Invalid input! Try again.")
                    continue    
                name = input("Please enter the account holder name: ")
                type_ = input("Please enter the type of account you want to open (Savings for Savings account or Chequing for Chequing account): ").capitalize()
                if type_ != "Savings" and type_ != "Chequing":
                    print("Invalid input! Try again.")
                    continue
                self.b.openAccount(num, name, interest, balance, type_)

            elif choice == "2" or choice == "Select Account":  #Searches for an account based on the account number, if it exists allows the user to work with it.
                while True:
                    try:
                        acc_num = int(input("Please enter the account number of the account that you want to work with: "))  #Gets the account number of the user's account.
                    except ValueError:
                        print("Invalid Input!")
                        continue
                    account = self.b.searchAccount(acc_num)
                    if account != -1:
                        self.showAccountMenu(account)
                    else:
                        print("Account does not exist.")    

            elif choice == "3" or choice == "Exit":
                break

            else:
                print("Invalid input! Please enter one of the options!")

    def showAccountMenu(self, account):
        """Loops to display the account options."""
        while True:
            print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit Account")
            choice = input("Please enter an option: ").title() 

            if choice == "1" or choice == "Check Balance":  #Prints the current balance of the account.
                print(account.getCurrentBalance())

            elif choice == "2" or choice == "Deposit":  #Deposits money to the account.
                try:
                    amount = int(input("Please enter the deposit amount: "))
                    if amount < 0:
                        print("Invalid input! Try again.")
                        continue
                except ValueError:
                    print("Invalid input! Try again.")
                    continue
                account.deposit(amount)

            elif choice == "3" or choice == "Withdraw":  #Withdraws money from the account.
                try:
                    amount = int(input("Please enter the withdrawal amount: "))
                    if amount < 0:
                        print("Invalid input! Try again.")
                        continue
                except ValueError:
                    print("Invalid input! Try again.")
                    continue
                account.withdraw(amount)

            elif choice == "4" or "Exit Account":
                self.showMainMenu()
                break

            else:
                print("Invalid input! Please enter one of the options!")

prog = Program()
prog.run()  #Runs the program.
