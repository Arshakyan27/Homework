# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero

class BankAccount:
    
    def __init__(self,account_number,balance) -> None:
        
        self.number = account_number
        self.balance = balance
    def get_balance(self):
        return f"{self.number},{self.balance}"
    def deposite(self,sum):
        if sum > 0:
            self.balance += sum
            return f"{self.number},{self.balance}"
        else:
            return "incorrect amount"
    def withdraw(self,sum1):
        
            self.balance -= sum1
            return f"{self.number},{self.balance}"
    
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance,int_rate) -> None:
        super().__init__(account_number, balance)
        self.interest = int_rate
    def deposite(self,amount):
        super().deposite(amount)
        interest = amount * (self.interest / 100)
        self.balance += interest
acc = SavingsAccount(12345,100,10)

class CheckingClass(BankAccount):
    def __init__(self, account_number, balance,overdraft_fee) -> None:
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee
    def withdraw(self,sum):
        super().withdraw(sum)
        if self.balance < 0:
            res = self.overdraft_fee * (sum / 100)
            self.balance -= res
            return f"New Balance: {self.balance}, Overdraft Fee: {self.overdraft_fee}"
acc = CheckingClass(12345,150,50)
print(acc.withdraw(200))
            