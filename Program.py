"""Contains the class program."""

from Bank import *

class Program:
    """Implements all the interaction between the user and the Bank."""

    def run(self):
        self.b = Bank()
        self.showMainMenu()

    def showMainMenu(self):
        while True:
            print("1. Open Account\n2. Select Account\n3. Exit")
            choice = input("Please enter an option: ").title()

            if choice == "1" or choice == "Open Account":
                pass

            elif choice == "2" or choice == "Select Account":
                while True:
                    try:
                        acc_num = int(input("Please enter the account number of the account that you want to work with: "))
                    except ValueError:
                        print("Invalid Input!")
                        continue
                    for account in self.b.accounts:
                        if account.getAccountNumber() == acc_num:
                            self.showAccountMenu(account)
                            return
            elif choice == "3" or choice == "Exit":
                break
            else:
                print("Invalid input! Please enter one of the options!")
