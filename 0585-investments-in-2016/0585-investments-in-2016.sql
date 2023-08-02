# Write your MySQL query statement below

-- tiv_2015 matches at least one other policyholder
-- unique (lat, lon)

SELECT ROUND(SUM(i1.tiv_2016), 2) AS tiv_2016
FROM Insurance i1
WHERE i1.tiv_2015 IN (
    SELECT i2.tiv_2015
    FROM Insurance i2
    GROUP BY i2.tiv_2015
    HAVING COUNT(DISTINCT i2.pid) > 1
)
AND (i1.lat, i1.lon) IN (
    SELECT i3.lat, i3.lon
    FROM Insurance i3
    GROUP BY i3.lat, i3.lon
    HAVING COUNT(DISTINCT i3.pid) = 1
);