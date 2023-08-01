# Write your MySQL query statement below

-- get max of numbers with count = 1

SELECT MAX(num) AS num
FROM (
    SELECT num, COUNT(num) AS cnt
    FROM MyNumbers
    GROUP BY num
    HAVING cnt = 1
) AS n;