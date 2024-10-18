# ===================================
# [Electronics Store]
# ===================================
# Developed by. [Elia Samuel]
# JCDS - [0412]

from tabulate import tabulate
from utils.dummy_data import get_dummy_data
from datetime import datetime
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
    """Displays a table of product information.

    Args:
        data (list): A list of dictionaries representing products.

    This function creates a table with the following columns:
    - ID
    - Name
    - Description
    - Price (Rp)
    - Stock
    - Category
    - Sales

    The table is formatted using the `tabulate` library.
    """
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
        for product in data
    ]

    headers = ["ID", "Name", "Description", "Price (Rp)", "Stock", "Category", "Sales"]
    print(tabulate(table_data, headers=headers, tablefmt="pretty",stralign='left'))

def sort_display_product_details():
    """Displays product details based on a given product ID.

    Args:
        product_id (int): The ID of the product to search for.

    This function searches for the product with the specified ID and displays its details in a table format if found. 
    If not found, an error message is printed.
    """
    input_id = get_user_int("Please Enter Product ID: ")
    product_found = find_product_by_id(input_id)

    if product_found:
        print("Product Details:")
        print(tabulate([[product_found["id"], product_found["name"], product_found["description"], 
                         product_found["price"], product_found["stock"], product_found["category"], product_found["sales"]]],
                         headers=["ID", "Product Name", "Description", "Price (Rp)", "Stock", "Category", "Sales"],
                         tablefmt="pretty"))
    else:
        print(f"Product ID {input_id} is not found")
    
def add_product():
    """Adds a new product to the database.

    This function prompts the user for product details and saves the new product if the user confirms.
    """
    input_id = get_user_int("Please Enter Product ID: ")
    isExists = get_unique_id(input_id)
    
    if not isExists:
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
            data.append(new_product)
            print("Product added successfully\n")
    else:
        print("Product ID already exists")
        add_product()

def find_product_by_id(input_id):
    """Finds a product in the database by its ID.

    Args:
        input_id (int): The ID of the product to search for.

    Returns:
        dict: The product object if found, otherwise None.
    """

    return next((product for product in data if product["id"] == input_id), None)

def get_unique_id(input_id):
    """Checks if a product ID is unique in the database.

    Args:
        input_id (int): The ID to check for uniqueness.

    Returns:
        bool: True if the ID is unique, False if it already exists.
    """
    return next((True for product in data if product["id"] == input_id), False)

def update_product():
    """Updates an existing product in the database.

    This function prompts the user for the product ID and allows them to modify specific product details.

    Args:
        product_id (int): The ID of the product to update.

    Returns:
        bool: True if the product was successfully updated, False otherwise.
    """
    input_id = get_user_int("Please Enter Product ID: ")
    isExists = get_unique_id(input_id)
    
    if not isExists:
        print(f"Product ID {input_id} not found")
        return
    
    product_found = next((product for product in data if product["id"] == input_id), None)

    if product_found:
        print("Current Product Details:")
        print(tabulate([[product_found["id"], product_found["name"], product_found["description"], 
                        product_found["price"], product_found["stock"], product_found["category"], product_found["sales"]]],
                        headers=["Product ID", "Product Name", "Description", "Price (Rp)", "Stock", "Category", "Sales"],
                        tablefmt="pretty"))
    
    input_confirm = confirm_data("Apakah anda melanjutkan proses update data?")

    if input_confirm:
        column_name = input("Enter Column Name: ")

        if column_name in product_found:
            new_data = input(f"Input New Data for {column_name}: ")
            if column_name in ["price", "stock", "sales"]: 
                new_data = get_user_int(new_data) 
            product_found[column_name] = new_data
            print("Product updated successfully.\n")
            print("Update Product Details")    
            print(tabulate([[product_found["id"], product_found["name"], product_found["description"], 
                    product_found["price"], product_found["stock"], product_found["category"], product_found["sales"]]],
                    headers=["Product ID", "Product Name", "Description", "Price (Rp)", "Stock", "Category", "Sales"],
                    tablefmt="pretty"))
        else:
            print("Invalid column name. Please try again.")
    else:
        ("Update Product Canceled")

def remove_product():
    """Removes a product from the database.

    This function prompts the user for the product ID and removes the corresponding product if it exists and the user confirms.

    Args:
        product_id (int): The ID of the product to remove.

    Returns:
        bool: True if the product was successfully removed, False otherwise.
    """
    input_id = get_user_int("Please Enter Product ID: ")
    isExists = get_unique_id(input_id)

    if isExists:
        input_confirm = confirm_data("You have entered new data. Would you like to save it?")
        if input_confirm:
            product_removed = find_product_by_id(input_id)
            if product_removed:
                data.remove(product_removed)
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
    data = get_dummy_data()
    
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