# Class
# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.

class BankAccount:
    
    def __init__(self,account_holder,balance) -> None:
        
        self.holder = account_holder
        self.balance = balance
    def get_balance(self):
        return f"{self.holder},{self.balance}"
    def deposite(self,sum):
        if sum > 0:
            self.balance += sum
            return f"{self.holder},{self.balance}"
        else:
            return "incorrect amount"
    def withdraw(self,sum1):
        if sum1 > self.balance:
            raise ValueError('There is not such money in your account')
        elif sum1 > 0:
            self.balance -= sum1
            return f"{self.holder},{self.balance}"
        
account1 = BankAccount("Davit",1000)
print(account1.get_balance())
print(account1.deposite(500))
print(account1.withdraw(200))