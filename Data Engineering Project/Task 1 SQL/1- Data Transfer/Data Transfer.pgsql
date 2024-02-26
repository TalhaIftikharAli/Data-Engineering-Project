-- Creating a new database
CREATE DATABASE customer_orders_db;

-- Creating tables
CREATE TABLE new_orders(
    customer_id VARCHAR(255),
    customer_name VARCHAR(255),
    order_id INTEGER,
    order_date DATE,
    shipment_date DATE,
    product_id VARCHAR(255),
    product_description TEXT,
    quantity INTEGER,
    unit_price FLOAT
)

-- Copying data from CSV to customer_orders_db
COPY new_orders
(
    customer_id, customer_name, order_id,
    order_date, shipment_date, product_id,
    product_description, quantity, unit_price
)
FROM 'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task SQL\0- Data Set\customer_dataset.csv'
DELIMITER ',' CSV HEADER;