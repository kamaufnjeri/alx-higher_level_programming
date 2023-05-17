-- Number of shows by genres
SELECT t.name AS genre,  COUNT(*) AS number_of_shows
FROM tv_genres t INNER JOIN tv_show_genres tg
ON t.id = tg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
