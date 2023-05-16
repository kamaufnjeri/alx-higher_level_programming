-- import to mysql database temp and find avg temp by city top three temps
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
