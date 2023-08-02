# Write your MySQL query statement below

-- first, get min year of each product
-- then get the quantity and price from this first year

SELECT s1.product_id, s2.first_year, s1.quantity, s1.price
FROM Sales AS s1
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) AS s2
ON s1.product_id = s2.product_id AND s1.year = s2.first_year