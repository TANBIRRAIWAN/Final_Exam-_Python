class User:
    def __init__(self, name,email,address,account_type,account_number) -> None:
        self.name = name 
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.__balance = 0
        self.transaction_history = 0
        self.loans_taken = 0

    def deposit(self,amount,bank):
        self.__balance += amount
        bank.get_bank_balance = amount
        self.transaction_history.append(("Deposit",amount))
        print("Your Bank Deposit is Successfull!!")

    def withdraw(self,amount,bank):
        if self.__balance >= amount:
            if bank.get_bank_balance > amount:
                self.__balance -= amount
                bank.get_bank_balance = - amount
                self.transaction_history.append(("withdraw",-amount))
                print(f"Withdraw Your Balance. Account Balance{self.__balance}")

            else:
                print(f" Bank is Bankrupt")

        else:
            print("Withdral amount exceeded !!") 


    def check_balance(self):
        print(f"Current Account Balance is : {self.__balance}")

    def check_transaction(self):
        print(f"TRANSACTION DETAILS :")
        for key,value in self.transaction_history:
            print(f"{key}\t\t\t {value}")


    def take_loan (self,amount,bank):
        if not bank.loan_feature_enabled:
            print("Loan feature is disable")
        elif self.loans_taken >=2:
            print("Your Loan withdraw time is Over !!")

        else:
            self.__balance += amount
            bank.get_bank_balance = -amount
            self.loans_taken += 1
            bank.total_loans += amount
            self.transaction_history.append(("Loan",amount))
            print(f"You have successfully receive your Loan")


    def balance_transfer(self,amount,other_account,bank):
        if other_account not in bank.accounts:
            print("Account does not exits")
        elif amount > self.__balance:
            print("Your balance amount is not sufficient !!")

        else:
            self.__balance -= amount
            bank.accounts[other_account].__balance += amount
            self.transaction_history.append((f"Transfer ({other_account})", -amount))
            bank.accounts[other_account].transaction_history.append((f"Received ({self.account_number})", +amount))
            print("Dear customer your balance transfer successfull!!")
            