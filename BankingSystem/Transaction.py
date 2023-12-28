class Transaction:
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.m = con.connect(user='root', password='root', port='3306', database='hmbank')
        self.cur = self.m.cursor()
        self.q2 = """
                            select * from transactions;
                        """
        self.cur.execute(self.q2)
        self.all = self.cur.fetchall()
        for i in self.all:
            if i[0] == self.transaction_id:
                self.customer_id = i[1]
                self.account_type = i[2]
                self.amount = i[3]
                self.transaction_type = i[4]

    def display_transaction_info(self):

        return f"Transaction ID: {self.transaction_id}\nCustomer ID: {self.customer_id}\n" \
               f"Account Type: {self.account_type}\nAmount: {self.amount}\n" \
               f"Transaction Type: {self.transaction_type}"
    
    
    
