-- Genres by rating
SELECT g.name, SUM(sr.rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON g.id = sg.genre_id
INNER JOIN tv_shows s
ON s.id = sg.show_id
INNER JOIN tv_show_ratings sr
ON s.id = sr.show_id
GROUP BY g.name
ORDER BY rating DESC;
