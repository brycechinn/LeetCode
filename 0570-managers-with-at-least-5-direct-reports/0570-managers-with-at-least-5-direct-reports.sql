# Write your MySQL query statement below

SELECT name
FROM Employee AS e
JOIN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
) AS m
ON e.id = m.managerId