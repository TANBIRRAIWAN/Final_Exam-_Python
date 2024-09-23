from user import User
from bank import Bank
from admin import Admin

dbbl = Bank("dbbl")
admin = Admin(dbbl)
users = {}


def admin_menu():
    while True:
        print("\n Admin Menu :")
        print("1. Create usere account ")
        print("2. Delete user account")
        print("3. View All Accounts")
        print("4. View Total Bank balance")
        print("5. view total loans")
        print("6. Toogle loan show")
        print("7. Exit!!")

        ch = int(input("Enter Your Input : "))

        if ch == 1:
            name = input("Enter Your Name :")
            email = input("Enter your E-mail : ")
            address = input("Enter your Address : ")
            account_type = input("Enter account type savings/current : ")
            admin.create_user_account(name,email,address,account_type)

        elif ch == 2:
            account_number = int(input("Enter Account number : "))
            admin.delete_user_account(account_number)

        elif ch ==3:
            admin.view_all_accounts()

        elif ch == 4:
            admin.view_total_bank_balance()

        elif ch == 5:
            admin.view_total_loans()

        elif ch == 6:
            admin.loan_feature()

        elif ch == 7:
            break

        else:
            print("Invalid Input")



def user_menu():
    while True:
        print("User Menu")
        print("1 . Deposit Money")
        print("2 . Withdraw money")
        print("3 . Check balance")
        print("4 . Check transaction history")
        print("5 . Take loan")
        print("6 . Transfer money")
        print("7 . Exit")

        ch = int(input("Enter your choice : "))

        if ch ==1:
            amount = float(input("Enter Amount :"))
            User.deposit(amount,dbbl) 

        elif ch ==2:
            amount = float(input("Enter Amount :"))
            User.withdraw(amount,dbbl)

        elif ch ==3:
            User.check_balance()              

        elif ch ==4:
            User.check_transaction()

        elif ch == 5:
            amount = float(input("Enter Amount : "))
            User.take_loan(amount,dbbl)

        elif ch ==6:
            amount = float (input("Enter amount to transfer : "))
            other_account = int (input("Enter receiver account number : "))
            User.balance_transfer(amount,other_account,dbbl) 

        elif ch ==7:
            break

        else:
            print("Invalid Input !!")




while True:
    print("Bank management System :")
    print("1. Admin Login")
    print("2.User Login")
    print("3. user registration")
    print("4.Exit")

    ch = int(input("Enter your choice : "))

    if ch==1:
        admin_menu()

    elif ch ==2 :
        account_number = int(input("Enter your Account Number : "))
        if account_number in dbbl.accounts:
            user = dbbl.accounts[account_number]
            user_menu()
        else:
            print(f"Account number is iccorrect!!")


    elif ch ==3:
        
        name = input("Enter Your Name :")
        email = input("Enter your E-mail : ")
        address = input("Enter your Address : ")
        account_type = input("Enter account type savings/current : ")
        account_number = dbbl.create_account(name,email,address,account_type)
        print(f"Your account number {account_number}")

    elif ch==4:
        break

    else:
        print("Invalid Input")