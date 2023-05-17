-- sum ratings for all shows
SELECT s.title, SUM(sr.rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings sr
ON s.id = sr.show_id
GROUP BY s.title
ORDER BY rating DESC;
