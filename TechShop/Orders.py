import mysql.connector as con


class Orders:
    def __init__(self, order_id):
        self.order_id = order_id
        self.m = con.connect(user='root', password='root', port='3306', database='TechShop')
        self.cur = self.m.cursor()
        self.q2 = """
                    select * from Orders;
                """
        self.cur.execute(self.q2)
        self.all = self.cur.fetchall()

        for i in self.all:
            if i[0] == self.order_id:
                self.customer_id = i[1]
                self.order_date = i[2]
                self.total_amount = i[3]

    def calculate_total_amount(self):
        total_amount = 0
        for order_detail in self.order_details:
            total_amount += order_detail.calculate_sub_total()
        return total_amount

    def get_order_details(self):
        details = f"Order ID: {self.order_id}\nOrder Date: {self.order_date}\nTotal Amount: {self.total_amount}\n"
        details += "Order Details:\n"
        for order_detail in self.order_details:
            details += order_detail.get_order_details_info() + "\n"
        return details

    def update_order_status(self, new_status):
        update_query = """
            UPDATE Orders
            SET status = %s
            WHERE orderid = %s;
        """
        update_data = (new_status, self.order_id)

        try:
            self.cur.execute(update_query, update_data)
            self.m.commit()
            return "Order status updated successfully."
        except con.Error as e:
            return f"Error updating order status: {e}"

    def cancel_order(self):
        cancel_query = """
            UPDATE Orders
            SET status = 'Cancelled'
            WHERE orderid = %s;
        """
        cancel_data = (self.order_id,)

        try:
            self.cur.execute(cancel_query, cancel_data)
            self.m.commit()
            return "Order cancelled successfully."
        except con.Error as e:
            return f"Error cancelling order: {e}"

