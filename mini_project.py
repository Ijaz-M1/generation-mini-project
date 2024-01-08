# import csv module

# testing to check if this commit change works
import csv

# create function to display dictionaries with their respected index value
def produce_pretty_list(input_list):
    output = ""
    for index, details in enumerate(input_list):
        output += f"Index: {index} Details: {details}\n"
    return output

# load content from .csv files
product_list = []
products_file = open("products.csv", "r")
p_file = csv.DictReader(products_file)
for products in p_file:
    product_list.append(products)

courier_list = []
couriers_file = open("couriers.csv", "r")
c_file = csv.DictReader(couriers_file)
for couriers in c_file:
    courier_list.append(couriers)

order_list = []
orders_file = open("orders.csv", "r")
o_file = csv.DictReader(orders_file)
for orders in o_file:
    order_list.append(orders)

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
            for product in product_list:
                print(product)

        # allows user to add a product and then prints new list
        elif menu == "2":
            product_name_input = input("Add a new product name: ")
            try:
                product_price_input = float(input("Add a price for the product: "))
            except ValueError:
                print("The input you entered is incorrect. Try again.")
                break
            new_product_dict = {"name": product_name_input, "price": product_price_input}
            product_list.append(new_product_dict)
            print("")
            # displays the list again
            for product in product_list:
                print(product)

        # update product name
        elif menu == "3":

            # print product indexes
            print(produce_pretty_list(product_list))

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
            for product in product_list:
                print(product)
            print("")
            print(produce_pretty_list(product_list))
            user_input = int(input("Enter the index value of your chosen product: "))
            del(product_list[user_input])
            for product in product_list:
                print(product)

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
            for courier in courier_list:
                print(courier)

        # allows user to add a courier and their phone number and then prints new list
        elif menu == "2":
            courier_name_input = input("Add a new courier name: ")
            try:
                courier_phone_input = int(input("Add a phone number for the courier: "))
            except ValueError:
                print("Please only input numbers")
                break
            new_courier_dict = {"name": courier_name_input, "phone": courier_phone_input}
            courier_list.append(new_courier_dict)
            print("")
            for courier in courier_list:
                print(courier)
            print("")

        # update courier name
        elif menu == "3":

            # print courier indexes
            print(produce_pretty_list(courier_list))

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
            for courier in courier_list:
                print(courier)
            print("")
            # display list of couriers with index values
            print(produce_pretty_list(courier_list))
            user_courier_input = int(input("Enter the index value of your chosen courier: "))
            del(courier_list[user_courier_input])
            print("")
            for courier in courier_list:
                print(courier)

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
            for order in order_list:
                print("")
                print(order)

        # allows user to add another dictionary and starts by inputting name, address and phone number
        elif order_menu == "2":

            customer_name = input("Please enter your name: ")
            customer_address = input("Please enter your full address: ")
            try:
                customer_phone = int(input("Please enter your phone number: "))
            except ValueError:
                print("Please only input numbers")
                print("")
                break


            # print product indexes
            print(produce_pretty_list(product_list))

            # input for comma-seperated list of product index values
            product_indexes = input("Enter product index numbers of the product that you chose. Split them using commas: ")

            # print courier indexes
            print(produce_pretty_list(courier_list))

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
            order_list.append(new_order)
            for order in order_list:
                print("")
                print(order)

        # prints order list with it's index value
        elif order_menu == "3":
            print(produce_pretty_list(order_list))

            user_order_input = int(input("Choose the index value of your chosen order: "))
            if user_order_input in range(len(order_list)):
                selected_order_index = order_list[user_order_input]
                print("The order you chose is: ", selected_order_index)
            else:
                print("This Index is invalid.")
                break

            # prints order status with it's index value
            print("")
            order_status_list = ['preparing', 'shipped', 'delivered', 'ordered']
            print(produce_pretty_list(order_status_list))

            # allows user to choose order status
            user_order_status_input = int(input("Enter the index value of your chosen order status: "))
            order_list[user_order_input]["status"] = order_status_list[user_order_status_input]
            for order in order_list:
                print("")
                print(order)

        # prints order list with index value
        elif order_menu == "4":
            print(produce_pretty_list(order_list))

            # allows user to choose the order by index value
            user_order_input = int(input("Enter the index value of your chosen order: "))
            if user_order_input in range(len(order_list)):
                selected_order_index = order_list[user_order_input]
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
            for order in order_list:
                print("")
                print(order)
            print("")
            print(produce_pretty_list(order_list))
            print("")
            user_order_input = int(input("Enter the index value of the order you want to delete: "))
            del(order_list[user_order_input])
            for order in order_list:
                print("")
                print(order)

        elif order_menu == "0":
            break

########################################################
# MAIN LOOP
########################################################
def main():
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
                writer.writerows(order_list)
            break

if __name__ == "__main__":
    main()