# Write your MySQL query statement below

-- just count managerId and if it's >= 5, output the manager's name

SELECT name
FROM Employee e
JOIN (
    SELECT managerId, COUNT(managerId) AS direct_reports
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
) m
ON e.id = m.managerId
WHERE direct_reports >= 5;