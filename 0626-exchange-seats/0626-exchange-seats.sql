# Write your MySQL query statement below

SELECT (
    CASE
        WHEN MOD(id, 2) != 0 AND cnt != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND cnt = id THEN id -- last seat same if odd
        ELSE id - 1
    END
) AS id, student
FROM
    Seat, (
        SELECT COUNT(*) AS cnt
        FROM Seat
    ) AS seat_counts
ORDER BY id;