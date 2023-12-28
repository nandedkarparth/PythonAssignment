import mysql.connector as con


class Customers:
    def __init__(self, customer_id):
        self.m = con.connect(user='root', password='root', port='3306', database='hmbank')
        self.cur = self.m.cursor()
        if customer_id == 'x':
            csid = int(input("Enter customer ID : "))
            fname = input("Enter first name : ")
            lname = input("Enter last name : ")
            dob = input("Enter dob in yyyy-mm-dd format")
            email = input("Enter email : ")
            phone = input("Enter phone no : ")
            q = """
                insert into customers values(%s,%s,%s,%s,%s,%s)
            """
            t = (csid, fname, lname, dob, email, phone)
            self.cur.execute(q, t)
            self.m.commit()
            print("Customer added successfully...")
            self.customer_id = csid
            self.first_name = fname
            self.last_name = lname
            self.dob = dob
            self.email = email
            self.phone = phone

        else:
            self.q2 = """
                        select * from Customers;
                    """
            self.cur.execute(self.q2)
            self.all = self.cur.fetchall()
            self.customer_id = customer_id

            for i in self.all:

                if i[0] == customer_id:
                    self.first_name = i[1]
                    self.last_name = i[2]
                    self.dob = i[3]
                    self.email = i[4]
                    self.phone = i[5]

    def show_info(self):
        return f"Customer: {self.first_name} {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nDOB: {self.dob}"

    
