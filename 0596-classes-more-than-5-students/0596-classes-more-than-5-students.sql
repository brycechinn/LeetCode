# Write your MySQL query statement below

SELECT class
FROM (
    SELECT class, COUNT(class) AS cnt
    FROM Courses
    GROUP BY class
) AS c
WHERE cnt >= 5;