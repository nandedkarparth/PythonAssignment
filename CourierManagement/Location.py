import mysql.connector as con


class Location:
    def __init__(self,locationid):
        self.m = con.connect(user='root', password='root', port='3306', database='courierms')
        self.cur = self.m.cursor()
        if locationid == 'x':
            self.locationid = int(input("Enter new location : "))
            self.name = input("Enter  location name : ")
            self.address = input("Enter address : ")
            self.q3 = """
                insert into users values(%s,%s,%s);
            """
            t = (self.locationid,self.name,self.address)
            self.cur.execute(self.q3,t)
            self.cur.commit()

        else:
            self.q2 = """
                        select * from location;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.locationid = locationid
            for i in self.all:
                if i[0] == locationid:
                    self.name = i[1]
                    self.address = i[2]


    def get_info(self):
        print( f"LocationID: {self.locationid} \nLocation Name:{self.name}\nAddress: {self.address}")


    
