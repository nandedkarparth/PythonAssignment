import mysql.connector as con


class Payment:
    def __init__(self,paymentid):
        self.m = con.connect(user='root', password='root', port='3306', database='courierms')
        self.cur = self.m.cursor()
        if paymentid == 'x':
            self.paymentid = int(input("Enter new paymentid"))
            self.courierid = input("Enter new courier id : ")
            self.locationid = input("Enter new locationid")
            self.amount = float(input("Enter amount : "))
            self.date = input("Enter payment date in yyyy-mm-dd format : ")
            self.q3 = """
                insert into users values(%s,%s,%s,%s,%s);
            """
            t = (self.paymentid,self.courierid,self.locationid,self.amount,self.date)
            self.cur.execute(self.q3,t)
            self.cur.commit()

        else:
            self.q2 = """
                        select * from payment;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.paymentid = paymentid
            for i in self.all:
                if i[0] == paymentid:
                    self.courierid = i[1]
                    self.locationid = i[2]
                    self.amount = i[3]
                    self.date = i[4]

    def get_info(self):
        print( f"PaymentID: {self.paymentid} \nCourierID:{self.courierid}\nLocationID: {self.locationid}\nAmount: {self.amount}\nPayment Date: {self.date}")



