# Write your MySQL query statement below

-- quality = AVG(rating / position)
-- poor_query_percentage = (percentage of all queries where rating < 3)
-- GROUP BY query_name

SELECT query_name, ROUND(AVG(rating / position), 2) AS quality, ROUND(SUM(rating < 3) / COUNT(query_name) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;