-- Inserting data to customers table
INSERT INTO database_schema.customers (customer_id, customer_name)
SELECT DISTINCT customer_id, customer_name
FROM public.customer_orders;

-- Inserting data to orders table
INSERT INTO database_schema.orders (order_id, customer_id, order_date, shipment_date)
SELECT DISTINCT ON (order_id) order_id, customer_id, order_date, shipment_date
FROM public.customer_orders;

-- -- Inserting data to products table
INSERT INTO database_schema.products (product_id, product_description, unit_price)
SELECT DISTINCT ON (product_id) product_id, product_description, unit_price
FROM public.customer_orders;

-- -- Inserting data to order_information table
INSERT INTO database_schema.order_information (order_id, product_id, quantity)
SELECT DISTINCT ON (order_id, product_id) order_id, product_id, quantity
FROM public.customer_orders
ORDER BY order_id, product_id;