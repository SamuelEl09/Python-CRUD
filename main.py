# ===================================
# [Electronics Store]
# ===================================
# Developed by. [Elia Samuel]
# JCDS - [0412]

from tabulate import tabulate
from utils.database import DbConnection
from operator import itemgetter
from utils.validation_func import get_user_options, get_user_int, confirm_data
import os


def clear_screen():
    os.system('cls')

# /===== Menu Program =====/
def main_menu():
    """Displays the main menu for the application.

    This function prints a menu with the following options:
    - View Product List
    - Add Product
    - Update Product
    - Remove Product
    - Exit
    """
    print(f"\n{'='*30}")
    print(f"{' '*10}Main Menu")
    print(f"{'='*30}")
    print("1. View Product List")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Remove Product")
    print("5. Exit\n")

def view_product_menu():
    """Displays a menu for viewing product information.

    This function presents users with options to:
    - Display all products
    - Find a product by its ID

    The user's choice determines the subsequent action.
    """
    while True:
        print(f"\n{'='*30}")
        print(f"{' '*7}View Product Menu")
        print(f"{'='*30}")
        print("1. Display All Product")
        print("2. Find Product by Product Id")
        print("3. Return to Main Menu\n")

        user_input = get_user_options(3)

        match user_input:
            case 1:
                view_product()
            case 2:
                sort_display_product_details()
                break
            case 3:
                clear_screen()
                break

def add_product_menu():
    """Displays a menu for adding products.

    This function presents users with options to:
    - Add a new product
    - Return to the main menu

    The user's choice determines the subsequent action.
    """
    while True:
        print(f"\n{'='*30}")
        print(f"{' '*7}Add Product Menu")
        print(f"{'='*30}")
        print("1. Add New Product")
        print("2. Return to Main Menu\n")

        user_input = get_user_options(2)

        match user_input:
            case 1:
                add_product()
            case 2:
                clear_screen()
                break

def update_product_menu():
    """Displays a menu for updating products.

    This function presents users with options to:
    - Update an existing product
    - Return to the main menu

    The user's choice determines the subsequent action.
    """
    while True:
        print(f"\n{'='*30}")
        print(f"{' '*5}Update Product Menu")
        print(f"{'='*30}")
        print("1. Update Product")
        print("2. Return to Main Menu\n")

        user_input = get_user_options(2)

        match user_input:
            case 1:
                update_product()
            case 2:
                clear_screen()
                break

def remove_product_menu():
    """Displays a menu for removing products.

    This function presents users with options to:
    - Remove a product from the store
    - Return to the main menu

    The user's choice determines the subsequent action.
    """
    while True:
        print(f"\n{'='*30}")
        print(f"{' '*5}Remove Product Menu")
        print(f"{'='*30}")
        print("1. Remove Product From Store")
        print("2. Return to Main Menu\n")

        user_input = get_user_options(2)

        match user_input:
            case 1:
                remove_product()
            case 2:
                clear_screen()
                break

# /===== Feature Program =====/
def view_product():
    products = data.show_data('product')
    table_data = [
        [
            product["id"],
            product["name"],
            product["description"],
            product["price"],
            product["stock"],
            product["category"],
            product["sales"]
        ]
        for product in products
    ]

    data_sorted = sorted(table_data,key=itemgetter(0))

    headers = ["ID", "Name", "Description", "Price (Rp)", "Stock", "Category", "Sales"]
    print(tabulate(data_sorted, headers=headers, tablefmt="pretty",stralign='left'))

def sort_display_product_details():

    input_id = get_user_int("Please Enter Product ID: ")
    product_found = get_product_by_id(input_id)

    if product_found:
        show_product_by_id("Product Details:",product_found)

    else:
        print(f"Product ID {input_id} is not found")
    
def add_product():
    input_id = get_user_int("Please Enter Product ID: ")
    exists = get_unique_id(input_id)
    
    if not exists:
        input_name = input("Please Enter Product Name: ")
        input_desc = input("Please Enter Product Description: ")
        input_price = get_user_int("Please Enter Product Price: ")
        input_stock = get_user_int("Please Enter Product Stock: ")
        input_category = input("Please Enter Product Category: ")
        input_sales = get_user_int("Please Enter Product Sales: ")

        input_confirm = confirm_data("You have entered new data. Would you like to save it?")

        if input_confirm:
            new_product ={
                    "id": input_id,
                    "name": input_name,
                    "description" : input_desc,
                    "price": input_price,
                    "stock": input_stock,
                    "category": input_category,
                    "sales": input_sales 
            }
            data.insert_one('product',new_product)
            print("Product added successfully\n")
    else:
        print(f"Product ID {input_id} already exists")
        add_product()

def get_product_by_id(input_id):
    return data.find_data_byId('product',{"id": input_id})

def get_unique_id(input_id):
    return data.find_data_byId('product',{"id": input_id}) is not None

def show_product_by_id(prompt, product):
    print(prompt)
    print(tabulate([[product["id"], product["name"], product["description"], 
        product["price"], product["stock"], product["category"], product["sales"]]],
        headers=["Product ID", "Product Name", "Description", "Price (Rp)", "Stock", "Category", "Sales"],
        tablefmt="pretty"))
    
def update_product():
    input_id = get_user_int("Please Enter Product ID: ")
    exists = get_unique_id(input_id)
    
    if not exists:
        print(f"Product ID {input_id} not found")
        return
    
    product_found =get_product_by_id(input_id)

    if product_found:
        show_product_by_id("Current Product Details:", product_found)

    input_confirm = confirm_data("Would you like to continue with the data update process?")

    if input_confirm:
        column_name = input("Enter Column Name: ").strip().lower()

        if column_name in product_found:
            new_data = input(f"Input New Data for {column_name}: ")
            if column_name in ["price", "stock", "sales"]:
                new_data = get_user_int(new_data)

            if confirm_data("Would you like to save the latest data?"):
                data.update_one('product', {'id': product_found['id']}, {column_name: new_data})
                updated_product =  get_product_by_id(input_id)
                show_product_by_id("Product Updated Successfully:", updated_product)

                print("Product updated successfully.")
            else:
                print("Update Product Canceled")
        else:
            print("Invalid column name. Please try again.")
    
def remove_product():
    input_id = get_user_int("Please Enter Product ID: ")
    exists = get_unique_id(input_id)

    if exists:
        input_confirm = confirm_data("Would you like to removed the product?")
        if input_confirm:
            product_removed = get_product_by_id(input_id)
            if product_removed:
                data.delete_one('product',product_removed)
                print(f"Product ID {input_id} has been removed successfully.")
            else:
                print("Error: Product not found after confirmation.")
        else:
            print("Product removal cancelled.")
    else:
        print(f"Product ID {input_id} does not exist.")

# /===== Main Program =====/
def main():
    """Function for main program
    """
    global data 
    data = DbConnection('localhost', 27017, 'dbcapstone')
    
    clear_screen()
    while True:
        main_menu()
        user_input = get_user_options(5)

        match user_input:
            case 1:
                clear_screen()
                view_product_menu()
            case 2:
                clear_screen()
                add_product_menu()
            case 3:
                clear_screen()
                update_product_menu()
            case 4:
                clear_screen()
                remove_product_menu()
            case 5:
                print("See Ya Capt!")
                return

if __name__ == "__main__":
    main()