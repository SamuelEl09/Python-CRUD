# dummy_laptops.py
# import tabulate

def get_dummy_data():
    # """
    # Retrieve dummy data for laptops.

    # Returns:
    #     dict: A dictionary containing a key 'laptops', which maps to a 
    #           list of laptop dictionaries.
    # """
    dummy_data = [
        {
            "id": 1,
            "name": "Laptop XYZ",
            "description": "Laptop with fast processor",
            "price": 10000000,
            "stock": 15,
            "category": "Electronics",
            "sales": 5
        },
        {
            "id": 2,
            "name": "Smartphone ABC",
            "description": "Smartphone with 48MP camera",
            "price": 3500000,
            "stock": 3,
            "category": "Electronics",
            "sales": 12
        },
        {
            "id": 3,
            "name": "Office Desk",
            "description": "Wooden desk for office",
            "price": 1200000,
            "stock": 10,
            "category": "Furniture",
            "sales": 3
        },
        {
            "id": 4,
            "name": "Ergonomic Chair",
            "description": "Comfortable chair for working",
            "price": 800000,
            "stock": 20,
            "category": "Furniture",
            "sales": 7
        },
        {
            "id": 5,
            "name": "Laser Printer",
            "description": "Printer for documents",
            "price": 2500000,
            "stock": 8,
            "category": "Electronics",
            "sales": 4
        },
        {
            "id": 6,
            "name": "24-inch Monitor",
            "description": "Full HD 24-inch monitor",
            "price": 1800000,
            "stock": 12,
            "category": "Electronics",
            "sales": 6
        },
        {
            "id": 7,
            "name": "Gaming Mouse",
            "description": "Mouse with high DPI",
            "price": 300000,
            "stock": 25,
            "category": "Accessories",
            "sales": 10
        },
        {
            "id": 8,
            "name": "Mechanical Keyboard",
            "description": "Mechanical keyboard with RGB",
            "price": 750000,
            "stock": 15,
            "category": "Accessories",
            "sales": 5
        },
        {
            "id": 9,
            "name": "Power Bank",
            "description": "10,000 mAh power bank",
            "price": 200000,
            "stock": 50,
            "category": "Accessories",
            "sales": 15
        },
        {
            "id": 10,
            "name": "HD Webcam",
            "description": "Webcam with HD quality",
            "price": 500000,
            "stock": 18,
            "category": "Electronics",
            "sales": 8
        }
        ]
    return dummy_data


# print(tabulate.__version__)