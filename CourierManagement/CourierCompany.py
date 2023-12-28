import mysql.connector as con


class CourierCompany:
    def __init__(self, serviceid):
        self.m = con.connect(user='root', password='root', port='3306', database='courierms')
        self.cur = self.m.cursor()
        if serviceid == 'x':
            self.serviceid = int(input("Enter new service id : "))
            self.name = input("Enter  service name : ")
            self.cost = float(input("Enter cost : "))
            self.q3 = """
                insert into users values(%s,%s,%s);
            """
            t = (self.serviceid, self.name, self.cost)
            self.cur.execute(self.q3, t)
            self.cur.commit()

        else:
            self.q2 = """
                        select * from courierservices;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.serviceid = serviceid
            for i in self.all:
                if i[0] == serviceid:
                    self.name = i[1]
                    self.cost = i[2]

    def get_info(self):
        print(f"ServiceID: {self.serviceid} \nService Name:{self.name}\nCost: {self.cost}")



