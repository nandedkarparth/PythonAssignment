import mysql.connector as con

from Products import Products


class OrderDetails:
    def __init__(self, order_details_id):
        self.order_details_id = order_details_id
        self.m = con.connect(user='root', password='root', port='3306', database='TechShop')
        self.cur = self.m.cursor()
        self.q2 = """
            select * from OrderDetails;
        """
        self.cur.execute(self.q2)
        self.all = self.cur.fetchall()

        for i in self.all:
            if i[0] == self.order_details_id:
                self.order_id = i[1]
                self.product_id = i[2]
                self.quantity = i[3]

    def get_order_details_info(self):
        return f"Order Details ID: {self.order_details_id}\nOrder ID: {self.order_id}\nProduct ID: {self.product_id}\nQuantity: {self.quantity}"

    def calculate_sub_total(self):
        product = Products(product_id=self.product_id)  # Create an instance of the Products class
        sub_total = product.price * self.quantity
        return sub_total

    def update_quantity(self, new_quantity):
        update_query = """
               UPDATE OrderDetails
               SET quantity = %s
               WHERE orderdetailsid = %s;
           """
        update_data = (new_quantity, self.order_details_id)

        try:
            self.cur.execute(update_query, update_data)
            self.m.commit()
            return "Quantity updated successfully."
        except con.Error as e:
            return f"Error updating quantity: {e}"

