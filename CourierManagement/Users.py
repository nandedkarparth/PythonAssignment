import mysql.connector as con


class Users:
    def __init__(self,userid):
        self.m = con.connect(user='root', password='root', port='3306', database='courierms')
        self.cur = self.m.cursor()
        if userid == 'x':
            self.userid = int(input("Enter new userid"))
            self.name = input("Enter Name : ")
            self.email = input("Enter email")
            self.password = input("Enter password : ")
            self.number = input("Enter contact number : ")
            self.address = input("Enter address : ")
            self.q3 = """
                insert into users values(%s,%s,%s,%s,%s,%s);
            """
            t = (self.userid,self.name,self.email,self.password,self.number,self.address)
            self.cur.execute(self.q3,t)
            self.cur.commit()

        else:
            self.q2 = """
                        select * from Users;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.userid = userid
            for i in self.all:
                if i[0] == userid:
                    self.name = i[1]
                    self.email = i[2]
                    self.password = i[3]
                    self.number = i[4]
                    self.address = i[5]


    def get_info(self):
        print( f"UserID: {self.userid} \nName:{self.name}\nEmail: {self.email}\nPhone: {self.number}\nAddress: {self.address}")



