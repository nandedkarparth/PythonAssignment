import mysql.connector as con
import Customer
import Account
import  Transaction
import myexceptions

while True:
    print("\nSelect an operation")
    print("1 - Withdrawal")
    print("2 - Deposit")
    print("3 - Balance Enquiry")
    print("4 - Open New Account")
    print("5 - View Transaction History")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        x = int(input("Enter Account Number : "))
        a = int(input("Enter Amount to withdraw : "))
        Account.Account(x).withdraw(a)
    elif ch==2:
        x = int(input("Enter Account Number : "))
        a = int(input("Enter Amount to deposit : "))
        Account.Account(x).deposit(a)
    elif ch==3:
        x = int(input("Enter Account Number : "))
        print(Account.Account(x).balance_enquiry())
    elif ch==4:
        Account.Account("x")
    elif ch==5:
        x = int(input("Enter Account Number : "))
        print(Account.Account(x).transaction_history())
    elif ch==0:
        exit(0)





