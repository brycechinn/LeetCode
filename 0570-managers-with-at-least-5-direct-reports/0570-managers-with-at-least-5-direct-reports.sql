# Write your MySQL query statement below

-- just count managerId and if it's >= 5, output the manager's name

SELECT name
FROM Employee AS e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
) AS m
ON e.id = m.managerId