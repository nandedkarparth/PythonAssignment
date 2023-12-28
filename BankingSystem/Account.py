import mysql.connector as con
import myexceptions as me

class Account:
    def __init__(self, account_id):
        self.account_id = account_id
        self.m = con.connect(user='root', password='root', port='3306', database='hmbank')
        self.cur = self.m.cursor()
        self.q2 = """
                    select * from Accounts;
                """
        self.cur.execute(self.q2)
        self.all = self.cur.fetchall()
        for i in self.all:
            if i[0] == self.account_id:
                self.customer_id = i[1]
                self.account_type = i[2]
                self.balance = i[3]
                self.transaction_date = i[4]
                self.pin = i[5]


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            q3 = """
                                update accounts set amount = %s where account_id = %s
                            """
            t = (self.balance, self.account_id)
            q4 = """
                                insert into transactions(account_id,transaction_type,amount,transaction_date) values (%s,"deposit",%s,curdate());
                            """
            t2 = (self.account_id, amount)
            self.cur.execute(q3, t)
            self.cur.execute(q4, t2)
            self.m.commit()
            print("Amount deposited successfully ")
            return True
        else:
            print("Invalid deposit amount.")
            return False
            raise me.InvalidDepositAmountError

    def withdraw(self, amount):
        pin = input("Enter PIN : ")
        print(self.pin)
        if pin == self.pin:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                q3 = """
                    update accounts set amount = %s where account_id = %s
                """
                t = (self.balance, self.account_id)
                q4 = """
                    insert into transactions(account_id,transaction_type,amount,transaction_date) values (%s,"deposit",%s,curdate());
                """
                t2 = (self.account_id, amount)
                self.cur.execute(q3, t)
                self.cur.execute(q4, t2)
                self.m.commit()
                print("Amount withdrawn")
                return True
            else:
                print("Invalid withdrawal amount or insufficient funds.")
                return False
                raise me.InvalidWithdrawalAmountError
        else:
            print("Enter valid PIN!")

    def balance_enquiry(self):
        pin = input("Enter PIN : ")
        if pin == self.pin:
            return self.balance
        else:
            print("Enter valid PIN")


    def transaction_history(self):
        pin = input("Enter PIN : ")
        if pin == self.pin:
            q3 = """
                select * from transactions where account_id = %s;
            """
            t = [self.account_id]
            self.cur.execute(q3, t)
            all = self.cur.fetchall()
            return all
        else:
            print("Enter valid PIN")







