# create product list
product_list = ["Black tea", "Americano", "Strawberry smoothie", "Avacado sandwich"]

# create courier list
courier_list = ["George", "Noah", "Sarah", "Henry"]

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
            product_list.append(input("Add a new product that you would like: "))
            print(product_list)

        # update product name
        elif menu == "3":

            # print product indexes
            for index, products in enumerate(product_list):
                print("Index: ", index, "Product: ", products)

            # allow user to choose product by index
            user_input = input("Enter the index value of your chosen product: ")
            user_index = int(user_input)
            if user_index in range(len(product_list)):
                selected_index_product = product_list[user_index]
                print("The product you chose is: ", selected_index_product)
            else:
                    print("This Index is invalid.")

            updated_product_name = input("What would you like to update the product name to be: ")
            product_list[user_index] = updated_product_name
            print(product_list)

        # delete a product
        elif menu == "4":
            print(product_list)
            for index, products in enumerate(product_list):
                print("Index: ", index, "Product: ", products)
            user_input = input("Enter the index value of your chosen product: ")
            user_index = int(user_input)
            del(product_list[user_index])
            print(product_list)

        # allows user to exit
        elif menu == "0":
            break

        # asks user to input a valid number and re prints menu to try again
        else:
            print("invalid number, please try again.")


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

        # allows user to add a courier and then prints new list
        elif menu == "2":
            courier_list.append(input("Add a new courier that you would like: "))
            print(courier_list)
            print("")

        # update courier name
        elif menu == "3":

            # print courier indexes
            for index, couriers in enumerate(courier_list):
                print("Index: ", index, "Courier: ", couriers)

            # allow user to choose courier by index
            user_courier_input = input("Enter the index value of your chosen courier: ")
            user_courier_index = int(user_courier_input)
            if user_courier_index in range(len(courier_list)):
                selected_index_courier = courier_list[user_courier_index]
                print("The courier you chose is: ", selected_index_courier)
            else:
                    print("This Index is invalid.")

            updated_courier_name = input("What would you like to update the courier name to be: ")
            courier_list[user_courier_index] = updated_courier_name
            print(courier_list)

        # delete a courier
        elif menu == "4":
            print(courier_list)
            for index, couriers in enumerate(courier_list):
                print("Index: ", index, "Courier: ", couriers)
            user_courier_input = input("Enter the index value of your chosen courier: ")
            user_courier_index = int(user_courier_input)
            del(courier_list[user_courier_index])
            print(courier_list)

        # allows user to exit
        elif menu == "0":
            break

        # asks user to input a valid number and re prints menu to try again
        else:
            print("invalid number, please try again.")


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

        # allows user to add another dictionary and sets the status to PREPARING
        elif order_menu == "2":
            user_order_dict = {
                "customer_name": input("Please enter your name: "),
                "customer_address": input("Please enter your full address: "),
                "customer_phone": input("Please enter your phone number: "),
                "status": "preparing"
            }
            order_dict.append(user_order_dict)
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
            user_order_input = int(input("Enter the index value of your chosen order: "))
            if user_order_input in range(len(order_dict)):
                selected_order_index = order_dict[user_order_input]
                print("The order you chose is: ", selected_order_index)
            else:
                    print("This Index is invalid.")
                    break

            # allows user to input the property they want to update
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

# main loop
while True:
    print(""" Ijaz's Coffee shop!
        1. Product menu
        2. Courier menu
        3. Order menu
        0. Exit""")

    menu = input("Choose your option: ")
    if menu == "1":
        product_menu()
    elif menu == "2":
        courier_menu()
    elif menu == "3":
        sub_menu()
    elif menu == "0":
        break
