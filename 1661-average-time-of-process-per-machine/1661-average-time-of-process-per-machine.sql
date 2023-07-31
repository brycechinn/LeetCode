# Write your MySQL query statement below

-- 1. get machine_id | process_id | processing time
-- 2. average processing time and group by machine_id

SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS 'processing_time'
FROM Activity a
JOIN Activity b
ON a.machine_id = b.machine_id 
WHERE a.process_id = b.process_id 
    AND a.activity_type = 'start'
    AND b.activity_type = 'end'
GROUP BY a.machine_id;