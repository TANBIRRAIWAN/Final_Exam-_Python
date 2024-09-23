from user import User
import random

class Bank:
    account_types = ["savings", "current"]
    def __init__(self,name) -> None:
        self.name = name
        self.accounts = {}
        self.total_loans = 0
        self.loan_feature_enabled = True
        self.__bank_balance = 1000

    def create_account(self,name,email,address,account_type):
        account_number = random.randint(150000,650000)

        if account_type.lower() in self.account_types:
            self.accounts[account_number] = User(name,email,address,account_type,account_number)
            print("Your Bank account is created")
            return account_number
        
        else:
            print("Account must be savings or current type account")


    #getter
    @property
    def get_bank_balance(self):
        return self.__bank_balance
    
    #setter
    @get_bank_balance.setter
    def get_bank_balance(self,amount):
        self.__bank_balance += amount

    #delete account
    def delete_account(self,account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account delet successfully !!")

        else:
            print("Account does not exit ")

    def account_list(self):
        print("Account name \t\t Email \t\t Account_type")
        for ket , user in self.accounts.items():
            print(f"{key}\t {user.name}\t{user.emil}\t{user.account_type}")


    def loan_feature_toggle(self):
        self.loan_feature_enabled = not self.loan_feature_enabled

        if self.loan_feature_enabled == True:
            print("Loan feature Enabled")

        else:
            print("Loan feature disabled") 


            
               