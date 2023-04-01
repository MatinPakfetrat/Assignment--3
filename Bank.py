"""Contains the class Bank."""

class SavingsAccount:
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
                