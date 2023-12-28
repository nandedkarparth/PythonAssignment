import mysql.connector as con


class Courier:
    def __init__(self,courierid):
        self.m = con.connect(user='root', password='root', port='3306', database='courierms')
        self.cur = self.m.cursor()
        if courierid == 'x':
            self.courierid = input("Enter Courier ID : ")
            self.sendername = input("Enter sender name : ")
            self.senderaddress = input("Enter sender address : ")
            self.receivername = input("Enter receiver name : ")
            self.receiveraddress = input("Enter receiver address : ")
            self.weight = input("Enter weight of courier : ")
            self.status = input("Enter status : ")
            self.trackingnumber = input("Enter tracking Number : ")
            self.deliverydate = input("Enter delivery date in yyyy-mm-dd format ")


            q3 = """
                insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """
            t = (self.courierid, self.sendername, self.senderaddress, self.receivername, self.receiveraddress, self.weight,self.trackingnumber,self.deliverydate)
            self.cur.execute(self.q3, t)
            self.cur.commit()

        else:
            self.q2 = """
                        select * from courier;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.courierid = courierid
            for i in self.all:
                if i[0] == courierid:
                    self.sendername = i[1]
                    self.senderaddress = i[2]
                    self.receivername = i[3]
                    self.receiveraddress = i[4]
                    self.weight = i[5]
                    self.status = i[6]
                    self.trackingnumber = i[7]
                    self.deliverydate = i[8]
    def get_info(self):
        print(f"CourierID: {self.courierid} \nSender Name:{self.sendername}\nSender Address : {self.senderaddress}\nReceiver Name: {self.receivername}\nReceiver Address: {self.receiveraddress}\nWeight :{self.weight}\nStatus :{self.status}\nTracking Number :{self.trackingnumber}\nDelivery Date :{self.deliverydate}")

