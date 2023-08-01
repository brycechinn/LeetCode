# Write your MySQL query statement below

-- count of unique products customer bought matches count of products

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);