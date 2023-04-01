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

            if choice == "1" or choice == "Open Account":
                pass

            elif choice == "2" or choice == "Select Account":
                while True:
                    try:
                        acc_num = int(input("Please enter the account number of the account that you want to work with: "))  #Gets the account number of the user's account.
                    except ValueError:
                        print("Invalid Input!")
                        continue
                    for account in self.b.accounts:  #Searches the accounts for the account that the user wants to work with.
                        if account.getAccountNumber() == acc_num:
                            self.showAccountMenu(account)

            elif choice == "3" or choice == "Exit":
                break

            else:
                print("Invalid input! Please enter one of the options!")

    def showAccountMenu(self, account):
        """Loops to display the account options."""
        while True:
            print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit Account")
            choice = input("Please enter an option: ").title() 
                       
            if choice == "1" or choice == "Check Balance":
                print(account.get_CurrentBalance())

            elif choice == "2" or choice == "Deposit":
                account.deposit()

            elif choice == "3" or choice == "Withdraw":
                account.withdraw()

            elif choice == "4" or "Exit Account":
                self.showMainMenu()
                break

            else:
                print("Invalid input! Please enter one of the options!")
