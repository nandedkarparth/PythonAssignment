import mysql.connector as con


class Customers:
    def __init__(self, customer_id):
        self.m = con.connect(user='root', password='root', port='3306', database='TechShop')
        self.cur = self.m.cursor()
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
                self.email = i[3]
                self.phone = i[4]
                self.address = i[5]

    def calculate_total_orders(self):
        q = """
        select count(%s) from orders where customerid = %s;
        """
        t = ['customerid',self.customer_id]
        self.cur.execute(q,t)
        print(self.cur.fetchall())

    def get_customer_details(self):
        return f"Customer: {self.first_name} {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"

    def update_customer_info(self, new_email, new_phone, new_address):
        update_query = """
            UPDATE Customers
            SET email = %s, phone = %s, address = %s
            WHERE customerid = %s;
        """
        update_data = (new_email, new_phone, new_address, self.customer_id)

        try:
            self.cur.execute(update_query, update_data)
            self.m.commit()
            return "Customer information updated successfully."
        except con.Error as e:
            return f"Error updating customer information: {e}"



