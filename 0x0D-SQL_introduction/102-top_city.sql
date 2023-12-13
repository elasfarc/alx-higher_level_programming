-- displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending)

SELECT city, avg(value) as avg_temp
FROM temperatures
WHERE month = 8 or month = 7
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
