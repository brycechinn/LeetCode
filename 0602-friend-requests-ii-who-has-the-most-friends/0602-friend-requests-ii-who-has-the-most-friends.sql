# Write your MySQL query statement below

SELECT user_id AS id, COUNT(*) AS num
FROM ((
    SELECT r1.requester_id AS user_id
    FROM RequestAccepted r1
) 
UNION ALL (
    SELECT r2.accepter_id
    FROM RequestAccepted r2
)) AS all_users
GROUP BY id
ORDER BY num DESC
LIMIT 1;