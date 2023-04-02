"""Contains the class Bank."""

class SavingsAccount:
    """Represents the savings accounts."""
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
    """Represents the chequing accounts."""
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
    """Represents a bank account."""
    def __init__(self, num, name, interest, balance, type_, minbal, overdraft):
        self.accountNumber = num
        self.accountHolderName = name.capitalize()
        self.rateOfInterest = interest
        self.currentBalance = balance
        if type_ == "Savings":
            self.acc = SavingsAccount(minbal)
        elif type_ == "Chequing":
            self.acc = ChequingAccount(overdraft)    

    def getAccountNumber(self):
        return self.accountNumber
    def getAccountHoldername(self):
        return self.accountHolderName
    def getRateOfInterest(self):
        return self.rateOfInterest
    def getCurrentBalance(self):
        return self.currentBalance
    
    def deposit(self, amount):
        self.currentBalance += amount
        print("Deposit successful! Current balance: {}".format(self.currentBalance))

    def withdraw(self, amount):
        self.currentBalance = self.acc.withdraw(self.currentBalance, amount)    

class Bank:
    """Implements the business logic required for the banking."""
    bankName = "TD Bank"        
    accounts = [Account(123, "matin", 2, 8000, "Savings", 3000, 5000), Account(456, "joe", 3, 9000, "Chequing", 4000, 4000),
                 Account(789, "mark", 1.5, 8500, "Savings", 2000, 4500), Account(141, "anna", 2.5, 9500, "Chequing", 3500, 4000),
                   Account(351, "sarah", 4, 7500, "Savings", 2500, 5000)]
    def openAccount(self, num, name, interest, balance, type_):
        for account in self.accounts:
            if account.getAccountNumber() == num:
                print("This account number already exists!")
                return
        self.accounts.append(Account(num, name, interest, balance, type_)) 
        print("Account created.")

    def searchAccount(self, num):
        for account in self.accounts:
            if account.getAccountNumber() == num:
                return account
        return -1    
    