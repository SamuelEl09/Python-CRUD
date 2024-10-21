def get_user_options(options):
    """Prompts the user to enter a valid option from a given range.

    Args:
        options (int): The maximum valid option number.

    Returns:
        int: The user's chosen option.
    """
    while True:
        try:
            user_input_menu = int(input("Enter your choice: "))
            if 1 <= user_input_menu <= options:
                return user_input_menu
            else:
                print("Invalid Selection!. Please enter a valid option.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

def get_user_int(prompt):
    """Prompts the user to enter a positive integer.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The user's entered positive integer value.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Value cannot be negative.\n")
                
        except ValueError:
            print("Error: Please enter a valid number.\n")

def confirm_data(prompt):
    while True:
        saved_data = input(f"{prompt} [Y/N]: ").strip().upper()
        if saved_data == 'Y':
            return True
        elif saved_data == 'N':
            print("Data failed to save.\n")
            return False
        else:
            print("Invalid Input! Please enter 'Y' for Yes or 'N' for No.\n")


