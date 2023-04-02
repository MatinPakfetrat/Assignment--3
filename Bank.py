"""Contains the class Bank."""

class SavingsAccount:
    """Extends the class Account to represent the savings accounts."""
    def __init__(self, minbal):
        self.minimumBalance = minbal

    def withdraw(self, balance, amount):
        if balance - amount < self.minimumBalance or balance < amount:
            print("Withdraw amount is too much!")
            return balance
        else:
            balance -= amount
            print("Withdrawal successful! Current balance: {}".format(balance))    
            return balance
                
class ChequingAccount:
    """Extends the class Account to represent the chequing accounts."""
    def __init__(self, overdraft):
        self.overdraftAllowed = overdraft                

    def withdraw(self, balance, amount):
        if amount > balance + self.overdraftAllowed:
            print("Withdraw amount is too much!")
            return balance

        else:
            balance -= amount
            print("Withdrawal successful! Current balance: {}".format(balance))
            return balance

class Account:
    def __init__(self, num, name, interest, balance, type_):
        self.accountNumber = num
        self.accountHolderName = name.capitalize()
        self.rateOfInterest = interest
        self.currentBalance = balance
        if type_ == "Savings":
            self.acc = SavingsAccount(3000)
        elif type_ == "Chequing":
            self.acc = ChequingAccount(5000)    

    def get_accountNumber(self):
        return self.accountNumber
    def get_accountHoldername(self):
        return self.accountHolderName
    def get_rateOfInterest(self):
        return self.rateOfInterest
    def get_currentBalance(self):
        return self.currentBalance
    
    def deposit(self, amount):
        self.currentBalance += amount
        print("Deposit successful! Current balance: {}".format(self.currentBalance))

    def withdraw(self, amount):
        self.currentBalance = self.acc.withdraw(self.currentBalance, amount)    

class Bank:
    """Implements the business logic required for the banking."""
    bankName = "TD Bank"        
    accounts = [Account(123, "matin", 2, 8000, "Savings"), Account(456, "joe", 3, 9000, "Chequing"),
                 Account(789, "mark", 1.5, 8500, "Savings"), Account(141, "anna", 2.5, 9500, "Chequing"),
                   Account(351, "sarah", 4, 7500, "Savings")]
    def openAccount(self, num, name, interest, balance, type_):
        for account in self.accounts:
            if account.get_accountNumber() == num:
                print("This account number already exists!")
                return
        self.accounts.append(Account(num, name, interest, balance, type_)) 
        print("Account created.")

    def searchAccount(self, num):
        for account in self.accounts:
            if account.get_accountNumber() == num:
                return account
        return -1    