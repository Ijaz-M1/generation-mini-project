# create product list
product_list = ["Black tea", "Americano", "Strawberry smoothie", "Avacado sandwich"]

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
            user_input = input("Choose the index value of your chosen product: ")
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
            user_input = input("Choose the index value of your chosen product: ")
            user_index = int(user_input)
            del(product_list[user_index])
            print(product_list)

        # allows user to exit
        elif menu == "0":
            break

        # asks user to input a valid number and re prints menu to try again
        else:
            print("invalid number, please try again.")

# main loop
while True:
    print(""" Ijaz's Coffee shop!
        1. Product menu
        2. Order menu
        0. Exit""")

    menu = input("Choose your option: ")
    if menu == "1":
        product_menu()
    elif menu == "0":
        break
