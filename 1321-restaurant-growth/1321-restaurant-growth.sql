# Write your MySQL query statement below

-- compute sum starting at 7th day, i.e. first day + 6 days



SELECT visited_on, (
    SELECT SUM(amount)
    FROM Customer c2
    WHERE c2.visited_on BETWEEN c1.visited_on - INTERVAL 6 DAY AND c1.visited_on
) AS amount, ROUND((
    SELECT SUM(amount) / 7
    FROM Customer c2
    WHERE c2.visited_on BETWEEN c1.visited_on - INTERVAL 6 DAY AND c1.visited_on
), 2) AS average_amount
FROM Customer c1
WHERE c1.visited_on - INTERVAL 6 DAY >= (
    SELECT MIN(c3.visited_on)
    FROM Customer c3
)
GROUP BY c1.visited_on;