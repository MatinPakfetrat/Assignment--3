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
    def __init__(self, num, name, interest, balance, type):
        self.accountNumber = num
        self.accountHolderName = name
        self.rateOfInterest = interest
        self.currentBalance = balance
        if type == "Savings":
            self.acc = SavingsAccount(5000)
        elif type == "Chequing":
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
        