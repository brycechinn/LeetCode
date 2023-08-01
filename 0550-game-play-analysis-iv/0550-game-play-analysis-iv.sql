# Write your MySQL query statement below

-- count number of players that logged in the day after they first logged in
-- divide by total number of players

SELECT ROUND(COUNT(a1.player_id) / (SELECT COUNT(DISTINCT a3.player_id) FROM Activity a3), 2) AS fraction
FROM Activity a1
WHERE (a1.player_id, a1.event_date - INTERVAL 1 DAY) IN (
    SELECT a2.player_id, MIN(a2.event_date)
    FROM Activity a2
    GROUP BY a2.player_id
);