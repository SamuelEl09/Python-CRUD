# Python CRUD Application for Electronic Store

A comprehensive Python application for managing Product data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the Electronic Store industry, specifically addressing the need to manage Product data efficiently. Product plays a crucial role in business processes as it directly impacts inventory management, sales forecasting, and customer satisfaction. 

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data

**Target Users:**

This application is designed for Staff and Store Owner within the organization to facilitate their tasks and activities related to product management.

## Features

* **Create:**
    * Add new Product entries with essential details like Product ID, Product Name, Descripion, Price, Stock, Category, and Sales.
    * Implement validation rules to ensure data integrity in the product management application. Unique Key for Product ID. Integer type data for Price, Stock and Sales. String type data for Product Name, Description and Category.   
* **Read:**
    * Search and retrieve specific Product records by applying filters based on Product ID.
    * Display comprehensive information for each Product in a user-friendly format.
* **Update:**
    * Modify existing Product data to reflect changes by column name.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted Product records with appropriate authorization checks.

## Installation

1. **Prerequisites:**
    * Python version 3.12.4

2. **Installation:**
    ```bash
    git clone https://github.com/SamuelEl09/Python_CRUD_Electronic_Store.git
    cd Python_CRUD_Electronic_Store
    ```
## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new Product record, for example, a new product in a inventory management system, providing details like name, price, stock, descriptive, category and sales.
    * **Read:** Search and retrieve prodcut information by product_id
    * **Update:** Modify product details, such as updating their name, price, stock, descriptive, category and sales.
    * **Delete:** Remove a product record from the system.

## Data Model
This project utilizes a List Of Dictionary data type to represent Product data. The following fields are typically stored:
   * [id]: (Int) - Unique Key for Product
   * [name]: (String) - for product's name
   * [description]: (String) - for the description of product
   * [price]: (Integer) - price of the product
   * [stock]: (Integer) - stock of the available product
   * [category]: (string) - category of the product
   * [sales]: (int) - total products that had been sold

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to samuelelia0907@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

