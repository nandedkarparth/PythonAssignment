import mysql.connector as con


class Products:
    def __init__(self, product_id):
        self.product_id = product_id
        self.m = con.connect(user='root', password='root', port='3306', database='TechShop')
        self.cur = self.m.cursor()
        self.q2 = """
            select * from Products;
        """
        self.cur.execute(self.q2)
        self.all = self.cur.fetchall()

        for i in self.all:
            if i[0] == self.product_id:
                self.product_name = i[1]
                self.description = i[2]
                self.price = i[3]

    def get_product_details(self):
        print( f"Product: {self.product_name}\nDescription: {self.description}\nPrice: {self.price}")

    def update_product_info(self, new_name, new_description, new_price):
        self.product_name = new_name
        self.description = new_description
        self.price = new_price

def is_product_in_stock(self):
    quantity_threshold = 0
    q = """
    SELECT quantity FROM Inventory WHERE productid = %s;
    """
    t = [self.product_id]

    try:
        self.cur.execute(q, t)
        quantity_available = self.cur.fetchone()[0]

        return quantity_available > quantity_threshold
    except con.Error as e:
        print(f"Error checking product stock: {e}")
        return False

