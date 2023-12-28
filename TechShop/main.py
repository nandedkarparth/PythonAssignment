import Products,Orders,OrderDetails, Inventory
import Customers as C

print("1.Manage Customers")
print("2.Manage Products")
print("3.Manage Orders")
print("4.Manage Order Details")
print("5.Manage Inventory")

while True:
    print("------------------------------------------")
    ch = int(input("Enter your choice : "))
    print("------------------------------------------")
    if ch == 1:
        csid = int(input("Enter Customer ID : "))
        print("1.Calculate Total Orders")
        print("2.Get Customer Details")
        print("3.Update Customer Info")
        customer_choice = int(input("Enter your choice : "))
        if customer_choice == 1:
            C.Customers(csid).calculate_total_orders()
        elif customer_choice == 2:
            print(C.Customers(csid).get_customer_details())
        elif customer_choice == 3:
            C.Customers(csid).update_customer_info()
        else :
            print("Enter Valid Choice !!")
    elif ch == 2:
        product_id = int(input("Enter Product ID : "))

        print("1. Get product details")
        print("2. Update product info")
        print("3. Check product availability")

        product_choice = int(input("Enter your choice: "))

        if product_choice == 1:
            Products.Products(product_id).get_product_details()
        elif product_choice == 2:
            Products.Products(product_id).update_product_info()
        elif product_choice == 3:
            Products.Products(product_id).is_product_in_stock()
        else:
            print("Enter Valid Choice !!")

    elif ch == 3:
        order_id = int(input("Enter Order ID : "))

        print("1. Calculate total amount")
        print("2. Get order details")
        print("3. Update order status")
        print("4. Cancel order")

        order_choice = int(input("Enter your choice: "))

        if order_choice == 1:
            Orders.Orders(order_id).calculate_total_amount()
        elif order_choice == 2:
            Orders.Orders(order_id).get_order_details()
        elif order_choice == 3:
            Orders.Orders(order_id).update_order_status()
        elif order_choice == 4:
            Orders.Orders(order_id).cancel_order()
        else:
            print("Enter Valid Choice !!")

    elif ch == 4:
        order_details_id = int(input("Enter Order Details ID : "))

        print("1. Calculate sub total")
        print("2. Get order details information")
        print("3. Update quanity")

        order_details_choice = int(input("Enter your choice: "))

        if order_details_choice == 1:
            OrderDetails.OrderDetails(order_details_id).calculate_sub_total()
        elif order_details_choice == 2:
            OrderDetails.OrderDetails(order_details_id).get_order_details_info()
        elif order_details_choice == 3:
            new_quantity = int(input("Enter new quantity: "))
            OrderDetails.OrderDetails(order_details_id).update_quantity(new_quantity)
        else:
            print("Enter Valid Choice !!")
    elif ch == 5:
        inventory_id = int(input("Enter Inventory ID: "))

        print("1. Add to inventory")
        print("2. Remove from inventory")
        print("3. Check product availibility")
        print("4. See low stock products")
        print("5. See out of stock products")
        print("6. See all products")
        print(("Press 0 to exit"))

        inventory_choice = int(input("Enter your choice: "))

        if inventory_choice == 1:
            quantity = int(input("Enter quantity to add to inventory: "))
            Inventory.Inventory(inventory_id).add_to_inventory(quantity)
        elif inventory_choice == 2:
            quantity = int(input("Enter quantity to remove from inventory: "))
            Inventory.Inventory(inventory_id).remove_from_inventory(quantity)
        elif inventory_choice == 3:
            Inventory.Inventory(inventory_id).is_product_available()
        elif inventory_choice == 4:
            threshold = int(input("Enter threshold value: "))
            Inventory.Inventory(inventory_id).list_low_stock_products(threshold)
        elif inventory_choice == 5:
            Inventory.Inventory(inventory_id).list_out_of_stock_products()
        elif inventory_choice == 6:
            Inventory.Inventory(threshold).list_all_product()
        else:
            print("Enter Valid Choice !!")
    elif ch == 0:
        exit(0)