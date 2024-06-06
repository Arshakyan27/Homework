# Create a class called BankAccount to represent a basic bank account. The class should
# have the following attributes:
# 1. owner: The name of the account owner.
# 2. balance: The current balance of the account.
# Implement the following methods:
# 1. __init__(self, owner, balance): Initializes the BankAccount object with the
# owner's name and initial balance. Ensure that the balance is a non-negative
# integer.
# 2. get_balance(self): Returns the current balance of the account.
# 3. deposit(self, amount): Adds the specified amount to the account balance.
# Ensure that the amount is a positive integer.
# 4. withdraw(self, amount): Subtracts the specified amount from the account
# balance. Ensure that the amount is a positive integer and does not exceed the
# current balance.
# Additionally, use @property and @attribute.setter to encapsulate the balance
# attribute and enforce validation rules.



class BankAccount:
    def __init__(self,owner,balance=0) -> None:
        if not isinstance(owner,str):
            raise TypeError("The owner's type should be string! ")
        if not isinstance(balance,int):
            raise TypeError("The balance's type should be integer! ")
        
        if balance < 0:
            raise ValueError("The balance can't be negative! ")
        self.__balance = balance
        self.owner = owner
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def get_balance(self,amount):
        if not isinstance(amount,int) or amount < 0:
            raise ValueError("Incorrect amount! ")
        self.__balance = amount
   
    
    
    def deposit(self,add):
        if not isinstance(add,int):
            raise TypeError("The added value's type should be inetger! ")
        if add > 0:
            ValueError("The number should be positive! ")
        self.__balance += add
    

    
    
    def withdraw(self,minus):
        if not isinstance(minus,int):
            raise TypeError("The withdraw's type should be integer! ")
        if minus < 0 or minus > self.__balance:
            raise ValueError("Incorrect amount! ")
        self.__balance -= minus

user = BankAccount('Sahak',500)
user.deposit = 200
print(user.balance)