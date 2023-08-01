# Write your MySQL query statement below

-- GROUP BY teacher_id

SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;