
-- SCHEMA: Database Schema
-- Step # 1
CREATE SCHEMA IF NOT EXISTS "database_schema"
    AUTHORIZATION postgres;

-- Selecting database_schema
SET search_path TO database_schema;

-- Step # 2
Creating TABLES
Creating Customers table
CREATE TABLE customers (
    customer_id VARCHAR(255) PRIMARY KEY,
    customer_name VARCHAR(255)
);

-- Creating Products table
CREATE TABLE products (
    product_id VARCHAR(255) PRIMARY KEY,
    product_description TEXT,
    unit_price DOUBLE PRECISION
);

-- Creating Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id VARCHAR(255) REFERENCES customers(customer_id),
    order_date DATE,
    shipment_date DATE
);

-- Creating order_information table
CREATE TABLE order_information (
    order_id INTEGER,
    product_id VARCHAR(255),
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);