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
            "product_id": 1,
            "product_name": "Laptop XYZ",
            "description": "Laptop with fast processor",
            "price": 10000000,
            "stock": 15,
            "date_received": "2024-10-01",
            "category": "Electronics",
            "sales": 5
        },
        {
            "product_id": 2,
            "product_name": "Smartphone ABC",
            "description": "Smartphone with 48MP camera",
            "price": 3500000,
            "stock": 30,
            "date_received": "2024-10-03",
            "category": "Electronics",
            "sales": 12
        },
        {
            "product_id": 3,
            "product_name": "Office Desk",
            "description": "Wooden desk for office",
            "price": 1200000,
            "stock": 10,
            "date_received": "2024-09-28",
            "category": "Furniture",
            "sales": 3
        },
        {
            "product_id": 4,
            "product_name": "Ergonomic Chair",
            "description": "Comfortable chair for working",
            "price": 800000,
            "stock": 20,
            "date_received": "2024-09-30",
            "category": "Furniture",
            "sales": 7
        },
        {
            "product_id": 5,
            "product_name": "Laser Printer",
            "description": "Printer for documents",
            "price": 2500000,
            "stock": 8,
            "date_received": "2024-10-05",
            "category": "Electronics",
            "sales": 4
        },
        {
            "product_id": 6,
            "product_name": "24-inch Monitor",
            "description": "Full HD 24-inch monitor",
            "price": 1800000,
            "stock": 12,
            "date_received": "2024-10-02",
            "category": "Electronics",
            "sales": 6
        },
        {
            "product_id": 7,
            "product_name": "Gaming Mouse",
            "description": "Mouse with high DPI",
            "price": 300000,
            "stock": 25,
            "date_received": "2024-10-04",
            "category": "Accessories",
            "sales": 10
        },
        {
            "product_id": 8,
            "product_name": "Mechanical Keyboard",
            "description": "Mechanical keyboard with RGB",
            "price": 750000,
            "stock": 15,
            "date_received": "2024-10-06",
            "category": "Accessories",
            "sales": 5
        },
        {
            "product_id": 9,
            "product_name": "Power Bank",
            "description": "10,000 mAh power bank",
            "price": 200000,
            "stock": 50,
            "date_received": "2024-09-29",
            "category": "Accessories",
            "sales": 15
        },
        {
            "product_id": 10,
            "product_name": "HD Webcam",
            "description": "Webcam with HD quality",
            "price": 500000,
            "stock": 18,
            "date_received": "2024-10-07",
            "category": "Electronics",
            "sales": 8
        }
        ]
    return dummy_data


# print(tabulate.__version__)