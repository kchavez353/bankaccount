class BankAccount:
        def __init__(self, int_rate, balance): 
                self.int_rate = int_rate
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount
                return self

        def withdraw(self, amount):
                self.balance -= amount 
                return self	

        def display_account_info(self):
                print(self.balance)

        def yield_interest(self):
                self.balance = self.balance + self.balance * self.int_rate
                self.display_account_info()

              

account1= BankAccount(0.01,200)
account2= BankAccount(0.02,400)

account1.deposit(20).deposit(40).deposit(20).withdraw(30).yield_interest()
account2.deposit(30).deposit(40).withdraw(10).withdraw(10).withdraw(10).withdraw(20).yield_interest()