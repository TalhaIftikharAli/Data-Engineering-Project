-- Query Optimization

SELECT customer_id, customer_name,
SUM(quantity * unit_price):: numeric AS total_purchases
FROM customer_orders
GROUP BY customer_id, customer_name
ORDER BY total_purchases DESC
LIMIT 5;