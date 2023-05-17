-- name all genres of a show Dexter
SELECT t.name
FROM tv_genres t INNER JOIN tv_show_genres tg
ON t.id = tg.genre_id
INNER JOIN tv_shows s
ON s.id = tg.show_id
WHERE s.title = 'Dexter';
