class Account:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  
        self.__balance = balance                

   
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

   
    def check_balance(self):
        print(f"Account Balance: {self.__balance}")
        return self.__balance


    def get_account_number(self):
        return self.__account_number




class Bank:
    def __init__(self):
        self.accounts= []


    def add_account(self,account):
        self.accounts.append(account)
        print(f"Account {account.get_account_number()} added to the bank.")

    
    def find_account(self,account_number):
        for account in self.accounts:
            if account.get_account_number == account_number:
                return account
            return None

    def total_assets(self):
        total=sum(account.check_balance() for account in self.accounts )
        print(f"Total assets in the bank is: {total}")
        return total


my_bank = Bank()

account1 = Account(account_number=101,balance=150)
account2 = Account(account_number=102,balance=200)

my_bank.add_account(account1)
my_bank.add_account(account2)

my_bank.total_assets()

