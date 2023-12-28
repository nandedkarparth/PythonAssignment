import mysql.connector as con


class Employee:
    def __init__(self,employeeid):
        self.m = con.connect(user='root', password='root', port='3306', database='courierms')
        self.cur = self.m.cursor()
        if employeeid == 'x':
            self.employeeid = int(input("Enter new employee id : "))
            self.name = input("Enter Name : ")
            self.email = input("Enter email")
            self.number = input("Enter contact number : ")
            self.role = input("Enter role of employee : ")
            self.salary = input("Enter salary of employee : ")
            self.q3 = """
                insert into employee values(%s,%s,%s,%s,%s,%s);
            """
            t = (self.employeeid,self.name,self.email,self.number,self.role,self.salary)
            self.cur.execute(self.q3,t)
            self.cur.commit()

        else:
            self.q2 = """
                        select * from employee;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.employeeid = employeeid
            for i in self.all:
                if i[0] == employeeid:
                    self.name = i[1]
                    self.email = i[2]
                    self.number = i[3]
                    self.role = i[4]
                    self.salary = i[5]


    def get_info(self):
        print( f"EmployeeID: {self.employeeid} \nName:{self.name}\nEmail: {self.email}\nPhone: {self.number}\nRole: {self.role}\nSalary: {self.salary}")




