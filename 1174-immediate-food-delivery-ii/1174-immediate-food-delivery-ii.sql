# Write your MySQL query statement below

SELECT ROUND((SUM(order_date = customer_pref_delivery_date) / COUNT(d.customer_id)) * 100, 2) AS immediate_percentage
FROM (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) AS f
JOIN Delivery AS d
ON f.customer_id = d.customer_id AND f.first_order_date = d.order_date;
