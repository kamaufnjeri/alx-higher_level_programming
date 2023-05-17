-- name all genres of a show
SELECT t.name
FROM tv_genres t INNER JOIN tv_show_genres tg
ON t.id = tg.genre_id
WHERE tg.show_id = 8;
