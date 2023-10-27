# import csv module
import csv

# load content from .csv files
product_file_list = []
products_file = open("products.csv", "r")
p_file = csv.reader(products_file, delimiter=",")
for products in p_file:
    product_file_list.append(products)

courier_file_list = []
couriers_file = open("couriers.csv", "r")
c_file = csv.reader(couriers_file, delimiter=",")
for couriers in c_file:
    courier_file_list.append(couriers)

order_file_list = []
orders_file = open("orders.csv", "r")
o_file = csv.reader(orders_file, delimiter=",")
for orders in o_file:
    order_file_list.append(orders)

# create product list
product_list = [
    {
    "name": "Black tea",
    "price": "1.50"
    },

    {
    "name": "Americano",
    "price": "1.80"
    },

    {
    "name": "Strawberry smoothie",
    "price": "1.20"
    },

    {
    "name": "Avacado sandwich",
    "price": "0.90"
    },
]

# create courier list
courier_list = [
    {
    "name": "George",
    "phone": "0798764325"
    },

    {
    "name": "Noah",
    "phone": "0798564356"
    },

    {
    "name": "Sarah",
    "phone": "0792346759"
    },

    {
    "name": "Henry",
    "phone": "0795637850"
    },

]

# create order dictionary
order_dict = [
    {
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "status": "preparing"
    },

    {
    "customer_name": "Sarah",
    "customer_address": "Apt 3B, 45 Elm Avenue, BIRMINGHAM, EX1 5YM",
    "customer_phone": "0798265177",
    "status": "shipped"
    },

    {
    "customer_name": "Michael",
    "customer_address": "Suite 5, 28 Oak Lane, MANCHESTER, AR1 8PK",
    "customer_phone": "0795863269",
    "status": "delivered"
    },

    {
    "customer_name": "Emily",
    "customer_address": "Flat 7, 9 Maple Street, LEEDS, QM9 6WS",
    "customer_phone": "0797572267",
    "status": "ordered"
    },
]

#############################################################################
# PRODUCT MENU
#############################################################################
def product_menu():
    while True:
        # print menu
        print(""" Ijaz's Coffee shop!
            1. Products
            2. Add new product!
            3. Update product
            4. Delete a product
            0. Exit""")

        # allow user to input value
        menu = input("Choose your option: ")
        if menu == "1":
            print(product_list)

        # allows user to add a product and then prints new list
        elif menu == "2":
            product_name_input = input("Add a new product name: ")
            product_price_input = input("Add a price for the product: ")
            new_product_dict = {"name": product_name_input, "price": product_price_input}
            product_list.append(new_product_dict)
            # displays the list again
            print(product_list)

        # update product name
        elif menu == "3":

            # print product indexes
            for index, products in enumerate(product_list):
                print("Index: ", index, "Product: ", products)

            # allow user to choose product by index
            user_input = int(input("Enter the index value of your chosen product: "))
            print("")
            if user_input in range(len(product_list)):
                selected_index_product = product_list[user_input]
                print("The product you chose is: ", selected_index_product)
            else:
                    print("This Index is invalid.")
                    break

            # allows user to update a value from the dictionary or skip it
            for key in selected_index_product:
                user_updated_product_property = input(f"Enter the updated value for {key} or press Enter to not update: ")
                if user_updated_product_property:
                    selected_index_product[key] = user_updated_product_property
                    print("Product property updated")
                    print(selected_index_product)
                else:
                    continue

        # delete a product
        elif menu == "4":
            print(product_list)
            for index, products in enumerate(product_list):
                print("Index: ", index, "Product: ", products)
            user_input = int(input("Enter the index value of your chosen product: "))
            del(product_list[user_input])
            print(product_list)

        # allows user to exit
        elif menu == "0":
            break

        # asks user to input a valid number and re prints menu to try again
        else:
            print("invalid number, please try again.")

##########################################################################
# COURIER MENU
##########################################################################
def courier_menu():
    while True:
        print(""" Courier menu!
            1. Couriers
            2. Add new courier!
            3. Update courier
            4. Delete a courier
            0. Exit""")

        # allow user to input value
        menu = input("Choose your option: ")
        if menu == "1":
            print(courier_list)

        # allows user to add a courier and their phone number and then prints new list
        elif menu == "2":
            courier_name_input = input("Add a new courier name: ")
            courier_phone_input = input("Add a phone number for the courier: ")
            new_courier_dict = {"name": courier_name_input, "phone": courier_phone_input}
            courier_list.append(new_courier_dict)
            print(courier_list)
            print("")

        # update courier name
        elif menu == "3":

            # print courier indexes
            for index, couriers in enumerate(courier_list):
                print("Index: ", index, "Courier: ", couriers)

            # allow user to choose courier by index
            user_courier_input = int(input("Enter the index value of your chosen courier: "))
            print("")
            if user_courier_input in range(len(courier_list)):
                selected_index_courier = courier_list[user_courier_input]
                print("The courier you chose is: ", selected_index_courier)
            else:
                    print("This Index is invalid.")
                    break

            # allows user to update a value from the dictionary or skip it
            for key in selected_index_courier:
                user_updated_courier_property = input(f"Enter the updated value for {key} or press Enter to not update: ")
                if user_updated_courier_property:
                    selected_index_courier[key] = user_updated_courier_property
                    print("Courier property updated")
                    print(selected_index_courier)
                else:
                    continue

        # delete a courier
        elif menu == "4":
            print(courier_list)
            # display list of couriers with index values
            for index, couriers in enumerate(courier_list):
                print("Index: ", index, "Courier: ", couriers)
            user_courier_input = int(input("Enter the index value of your chosen courier: "))
            del(courier_list[user_courier_input])
            print(courier_list)

        # allows user to exit
        elif menu == "0":
            break

        # asks user to input a valid number and re prints menu to try again
        else:
            print("invalid number, please try again.")

#########################################################################
# ORDER MENU
#########################################################################
def sub_menu():
    while True:
        # print menu
        print(""" Order Menu!
            1. Order Menu
            2. Create an order
            3. Update existing order status
            4. Update existing order
            5. Delete an order
            0. Return to main menu""")

        order_menu = input("Choose your option: ")
        # print order dictionary
        if order_menu == "1":
            print(order_dict)

        # allows user to add another dictionary and starts by inputting name, address and phone number
        elif order_menu == "2":

            customer_name = input("Please enter your name: ")
            customer_address = input("Please enter your full address: ")
            customer_phone = input("Please enter your phone number: ")


            # print product indexes
            for index, products in enumerate(product_list):
                print("Index: ", index, "Product: ", products)

            # input for comma-seperated list of product index values
            product_indexes = input("Enter product index numbers of the product that you chose. Split them using commas: ")

            # print courier indexes
            for index, couriers in enumerate(courier_list):
                print("Index: ", index, "Courier: ", couriers)

            # allow user to choose courier by index
            user_courier_input = int(input("Enter the index value of your chosen courier: "))
            print("")
            if user_courier_input in range(len(courier_list)):
                courier_name = courier_list[user_courier_input]["name"]
                print("The courier you chose is: ", courier_name)
            else:
                    print("This Index is invalid.")
                    break

            # creates a new order dictionary with the addition of items and courier
            # it also sets the default status to 'preparing'
            new_order = {
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "items": product_indexes,
                "courier": user_courier_input,
                "status": "preparing"
            }

            # combines the dictionary created above to the list of dictionaries created at the beginning
            order_dict.append(new_order)
            print(order_dict)

        # prints order list with it's index value
        elif order_menu == "3":
            for index, order in enumerate(order_dict):
                print("Index: ", index, "Order: ", order)

            user_order_input = int(input("Choose the index value of your chosen order: "))
            if user_order_input in range(len(order_dict)):
                selected_order_index = order_dict[user_order_input]
                print("The order you chose is: ", selected_order_index)
            else:
                print("This Index is invalid.")
                break

            # prints order status with it's index value
            print("")
            order_status_list = ['preparing', 'shipped', 'delivered', 'ordered']
            for index, order_status in enumerate(order_status_list):
                print(index,": ", order_status)

            # allows user to choose order status
            user_order_status_input = int(input("Enter the index value of your chosen order status: "))
            order_dict[user_order_input]["status"] = order_status_list[user_order_status_input]
            print(order_dict)

        # prints order list with index value
        elif order_menu == "4":
            for index, order in enumerate(order_dict):
                print("Index: ", index, "Order: ", order)

            # allows user to choose the order by index value
            user_order_input = int(input("Enter the index value of your chosen order: "))
            if user_order_input in range(len(order_dict)):
                selected_order_index = order_dict[user_order_input]
                print("The order you chose is: ", selected_order_index)
            else:
                    print("This Index is invalid.")
                    break

            # allows user to update a value from the dictionary or skip it
            for key in selected_order_index:
                user_updated_order_property = input(f"Enter the updated value for {key} or press Enter to not update: ")
                if user_updated_order_property:
                    selected_order_index[key] = user_updated_order_property
                    print("Order property updated")
                    print(selected_order_index)
                else:
                    continue

        # allows user to delete an order
        elif order_menu == "5":
            print(order_dict)
            print("")
            for index, order in enumerate(order_dict):
                print("Index: ", index, "Order: ", order)
            print("")
            user_order_input = int(input("Enter the index value of the order you want to delete: "))
            del(order_dict[user_order_input])
            print(order_dict)

        elif order_menu == "0":
            break

########################################################
# MAIN LOOP
########################################################
while True:
    print(""" Ijaz's Coffee shop!
        1. Product menu
        2. Courier menu
        3. Order menu
        0. Exit""")

    # allows user to choose which menu they want to go into
    menu = input("Choose your option: ")
    if menu == "1":
        product_menu()
    elif menu == "2":
        courier_menu()
    elif menu == "3":
        sub_menu()
    elif menu == "0":

        # saves any updates or changes to the .csv files and finally ends the program
        with open("products.csv", "w") as products_file:
            fieldnames = ["name", "price"]
            writer = csv.DictWriter(products_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(product_list)

        with open("couriers.csv", "w") as couriers_file:
            fieldnames = ["name", "phone"]
            writer = csv.DictWriter(couriers_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(courier_list)

        with open("orders.csv", "w") as orders_file:
            fieldnames = ["customer_name", "customer_address", "customer_phone", "items", "courier", "status"]
            writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(order_dict)
        break