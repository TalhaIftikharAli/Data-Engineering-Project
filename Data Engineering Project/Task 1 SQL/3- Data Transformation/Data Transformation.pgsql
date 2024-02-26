-- Data Transformation

SELECT product_id, product_description,
SUM(quantity * unit_price):: numeric AS total_revenue
FROM customer_orders
GROUP BY product_id, product_description
ORDER BY total_revenue DESC;