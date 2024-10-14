# ===================================
# [Electronics Store]
# ===================================
# Developed by. [Elia Samuel]
# JCDS - [0412]

from tabulate import tabulate
from utils.dummy_data import get_dummy_data
import os

# /===== Feature Program =====/
def view_product():
    """
    Display the list of products in a formatted table.

    This function retrieves all products from the global `data` list 
    and displays their details in a structured table format using the 
    `tabulate` library. The table includes
    """
    table_data = [
        [
            product["product_id"],
            product["product_name"],
            product["description"],
            product["price"],
            product["stock"],
            product["date_received"],
            product["category"],
            product["sales"]
        ]
        for product in data
    ]

    headers = ["Product ID", "Product Name", "Description", "Price (Rp)", "Stock", "Date Received", "Category", "Sales"]
    print(tabulate(table_data, headers=headers, tablefmt="pretty",stralign='left'))

def sort_data_by_id(input_id):
    for product in data:
        if product["product_id"] == input_id:
            print(tabulate([[product["product_id"], product["product_name"], product["description"], 
                             product["price"], product["stock"], product["date_received"], 
                             product["category"], product["sales"]]],
                             headers=["Product ID", "Product Name", "Description", "Price (Rp)", "Stock", "Date Received", "Category", "Sales"],
                             tablefmt="pretty"))
            return True
        
    return False

def add_product(input_id, input_name, input_desc, input_price, input_stock, input_date_received, 
                input_category, input_sales):
    """
    Add a new product to the product list.

    This function creates a new product represented as a dictionary 
    with the specified attributes and adds it to the global list of products.

    The function assumes that the global variable `data` is a list of dictionaries,
    where each dictionary represents a product.

    Args:
        input_id (str): Unique identifier for the product.
        input_name (str): Name of the product.
        input_desc (str): Description of the product.
        input_price (float): Price of the product (in Rp).
        input_stock (int): Available stock of the product.
        input_date_received (str): Date the product was received (in YYYY-MM-DD format).
        input_category (str): Category of the product.
        input_sales (int): Number of products sold.

    Returns:
        None

    """
    new_product ={
            "product_id": input_id,
            "product_name": input_name,
            "description" : input_desc,
            "price": input_price,
            "stock": input_stock,
            "date_received": input_date_received,
            "category": input_category,
            "sales": input_sales 
    }
    
    data.append(new_product)
    print("Product added successfully\n")
    view_product()

def update_product(input_id):
    """
    Update product details based on the provided product ID.

    This function searches for a product with the given `input_id` in the 
    global `data` list and allows the user to update various details of 
    the product. If the product is found, it displays the current details 
    and prompts the user for new information. If the user leaves an input 
    empty, the current value for that field remains unchanged.

    Args:
        input_id (int/str): The ID of the product to update.

    Returns:
        None
    """
    product_found = None

    for product in data:
        if product["product_id"] == input_id:
            product_found = product
            break

    if product_found:
        print("Current Product Details:")
        print(tabulate([[product_found["product_id"], product_found["product_name"], product_found["description"], 
                         product_found["price"], product_found["stock"], product_found["date_received"], 
                         product_found["category"], product_found["sales"]]],
                         headers=["Product ID", "Product Name", "Description", "Price (Rp)", "Stock", "Date Received", "Category", "Sales"],
                         tablefmt="pretty"))
    
        input_name = input("Please Enter Product Name (leave empty to keep current): ")
        input_desc = input("Please Enter Product Description (leave empty to keep current): ")
        input_price = input("Please Enter Product Price (leave empty to keep current): ")
        input_stock = input("Please Enter Product Stock (leave empty to keep current): ")
        input_date_received = input("Please Enter Product Date Received (leave empty to keep current): ")
        input_category = input("Please Enter Product Category (leave empty to keep current): ")
        input_sales = input("Please Enter Product Sales (leave empty to keep current): ")

        if input_name:
            product_found["product_name"] = input_name
        if input_desc:
            product_found["description"] = input_desc
        if input_price:
            product_found["price"] = int(input_price) 
        if input_stock:
            product_found["stock"] = int(input_stock)
        if input_date_received:
            product_found["date_received"] = input_date_received
        if input_category:
            product_found["category"] = input_category
        if input_sales:
            product_found["sales"] = int(input_sales)

        print("Product details updated successfully.\n")
        view_product()
    else:
        print("Error: Product is not Found")

def delete_product(input_id):
    """
    Delete a product from the data list based on the provided product ID.

    This function searches for a product with the given `input_id` in the 
    global `data` list. If the product is found, it removes the product 
    from the list and displays the updated list of products.

    Args:
        input_id (int/str): The ID of the product to delete.

    Returns:
        None
    """
    for product in data:
        if input_id == product["product_id"]:
            data.remove(product)
            print(f"Product ID {input_id} has been removed successfully")
            view_product()
            return
    
    print("Error: Product ID is not Found")
            

# /===== Main Program =====/
def main():
    """Function for main program
    """
    global data 
    data = get_dummy_data()

    while True:
        print(f"\n{'='*30}")
        print(f"{' '*10}Main Menu")
        print(f"{'='*30}")
        print("1. View Product List")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Remove Product")
        print("5. Exit\n")

        try:
            user_input_menu = int(input("Enter your choice: "))
            if user_input_menu == 1:
                os.system("cls")
                while True:
                    print(f"\n{'='*30}")
                    print(f"{' '*7}View Product Menu")
                    print(f"{'='*30}")
                    print("1. Display All Product")
                    print("2. Find Product by Product Id")
                    print("3. Return to Main Menu\n")

                    try:
                        user_input_menu_view = int(input("Enter your choice: "))

                        if user_input_menu_view == 1:
                            view_product()
                        elif user_input_menu_view == 2:
                            while True:
                                try: 
                                    find_product_id = int(input("Please Enter Product ID: "))

                                    if not sort_data_by_id(find_product_id):
                                        print(f"Error: Product ID {find_product_id} is not found.")

                                except ValueError:
                                    print("Error: Please enter a valid Product ID")
                                    break
                                else:
                                    break
                        elif user_input_menu_view == 3:
                            os.system("cls")
                            break
                        else: 
                            print("Error: Please enter a valid option")
                    except ValueError:
                        print("Error: Please enter a number corresponding to the menu options ")

            elif user_input_menu == 2:
                os.system("cls")
                while True:
                    print(f"\n{'='*30}")
                    print(f"{' '*7}Add Product Menu")
                    print(f"{'='*30}")
                    print("1. Add New Product")
                    print("2. Return to Main Menu\n")

                    try:
                        user_input_menu_add = int(input("Enter your choice: "))

                        if user_input_menu_add == 1:
                            while True: 
                                try:
                                    input_id = int(input("Please Enter Product ID: "))
                                    if any(product["product_id"] == input_id for product in data):
                                        print(f"Error: Product ID {input_id} already exist.")
                                        continue
                                    break
                                except ValueError:
                                    print("Error: Please enter a number for the Product ID.")
                        
                            input_name = input("Please Enter Product Name: ")
                            input_desc = input("Please Enter Product Description: ")
                            input_price = input("Please Enter Product Price: ")
                            input_stock = input("Please Enter Product Stock: ")
                            input_date_received = input("Please Enter Product Date Received: ")
                            input_category = input("Please Enter Product Category: ")
                            input_sales = input("Please Enter Product Sales: ")

                            while True:
                                saved_data = input("Is the data correct and ready to be saved? [Y/N]: ")
                                if saved_data == 'Y':
                                    add_product(input_id, input_name, input_desc, input_price, input_stock, input_date_received, input_category, input_sales)
                                    break
                                elif saved_data == 'N':
                                    print("Data failed to save.")
                                    break
                                else:
                                    print("Error: Invalid Input. Please enter 'Y' for Yes or 'N' for No.")
                        elif user_input_menu_add == 2:
                            os.system("cls")
                            break
                        else:
                            print("Error: Please enter a valid option ")
                    except ValueError:
                        print("Error: Please enter a number corresponding to the menu options ")

            elif user_input_menu == 3:
                os.system("cls")
                while True:
                    print(f"\n{'='*30}")
                    print(f"{' '*5}Update Product Menu")
                    print(f"{'='*30}")
                    print("1. Update Product")
                    print("2. Return to Main Menu\n")

                    user_input_menu_update = int(input("Enter your choice: "))
                    if user_input_menu_update == 1:
                        try:

                            input_id = int(input("Please Input Product ID: "))
                            update_product(input_id)
                            
                        except ValueError:
                            print("Invalid Input, please enter the data in the correct format.")

                    elif user_input_menu_update == 2:
                        os.system("cls")
                        break
                    else:
                        print("Error: Please enter a valid option")
            elif user_input_menu == 4:
                os.system("cls")
                while True:
                    print(f"\n{'='*30}")
                    print(f"{' '*5}Remove Product Menu")
                    print(f"{'='*30}")
                    print("1. Remove Product From Store")
                    print("2. Return to Main Menu\n")

                    try:
                        user_input_menu_remove = int(input("Enter your choice: "))
                        if user_input_menu_remove == 1:    
                            view_product()                        
                            while True:
                                try:
                                    input_id = int(input("Please Input Product ID: "))
                                    product_exists = any(product["product_id"] == input_id for product in data)
                                    
                                    if product_exists:
                                        confirm = input(f"Are you sure you want to remove the product with ID {input_id}? [Y/N]: ").strip().upper()
                                        if confirm == 'Y':
                                            if delete_product(input_id): 
                                                print("Product removed successfully.")
                                            break 
                                        elif confirm == 'N':
                                            print("Product removal canceled.")
                                            break
                                        else:
                                            print("Error: Invalid Input. Please enter 'Y' for Yes or 'N' for No.")
                                    else:
                                        print("Error: Product ID is not found.")
                                except ValueError:
                                    print("Error: Please Input Valid Product ID")

                        elif user_input_menu_remove == 2:
                            print("Thank yaa")
                            break
                        else:
                            print("Error: Please enter a valid option")
                    
                    except ValueError:
                        print("Error: Please enter a number corresponding to the menu options ")

            elif user_input_menu == 5:
                print("Exiting...")
                break
            else:
                print("Error: Please enter a valid option")

        except ValueError:
            print("Error: Please enter a number corresponding to the menu options ")

if __name__ == "__main__":
    main()