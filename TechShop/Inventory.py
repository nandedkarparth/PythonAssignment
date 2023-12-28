import mysql.connector as con


class Inventory:
    def __init__(self, inventory_id):
        self.inventory_id = inventory_id
        self.m = con.connect(user='root', password='root', port='3306', database='TechShop')
        self.cur = self.m.cursor()
        self.q2 = """
            select * from Inventory;
        """
        self.cur.execute(self.q2)
        self.all = self.cur.fetchall()

        for i in self.all:
            if i[0] == inventory_id:
                self.product_id = i[1]
                self.quantity_in_stock = i[2]
                self.last_stock_update = i[3]

    def add_to_inventory(self, quantity):
        self.quantity_in_stock = self.quantity_in_stock + quantity
        q3 = """
            update Inventory set QuantityInStock = %s, LastStockUpdate = now() where InventoryID = %s;
        """
        t = (self.quantity_in_stock,self.inventory_id)
        self.cur.execute(q3,t)
        self.m.commit()

    def remove_from_inventory(self, quantity):
        self.quantity_in_stock = self.quantity_in_stock - quantity
        q3 = """
                    update Inventory set QuantityInStock = %s, LastStockUpdate = now() where InventoryID = %s;
                """
        t = (self.quantity_in_stock, self.inventory_id)
        self.cur.execute(q3, t)
        self.m.commit()


    def is_product_available(self):
        if self.quantity_in_stock > 0:
            return True
        else:
            return False



    def list_low_stock_products(self, threshold):
        q3 = """
            SELECT p.productname, i.quantityinstock,i.laststockupdate
            FROM inventory i
            JOIN Products p ON i.productid = p.productid
            WHERE i.quantityinstock <= %s
        """
        t = [threshold]
        self.cur.execute(q3,t)
        all = self.cur.fetchall()
        for i in all:
            print(i)

    def list_out_of_stock_products(self):
        q3 = """
            SELECT p.productname, i.quantityinstock,i.laststockupdate
            FROM inventory i
            JOIN Products p ON i.productid = p.productid
            WHERE i.quantityinstock <=0
        """
        self.cur.execute((q3))
        all = self.cur.fetchall()
        for i in all:
            print(i)

    def list_all_product(self):
        q3 = """
            SELECT p.productname, i.quantityinstock,i.laststockupdate
            FROM inventory i
            JOIN Products p ON i.productid = p.productid;
        """
        self.cur.execute((q3))
        all = self.cur.fetchall()
        for i in all:
            print(i)
