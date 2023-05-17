-- Lists all genres not in Dexter
SELECT DISTINCT s.name
FROM tv_genres g
INNER JOIN tv_show_genres s
ON g.id = s.genre_id
INNER JOIN tv_shows t
ON s.show_id = t.id
WHERE g.name NOT IN(
	SELECT g.name
        FROM tv_genres g
	INNER JOIN tv_show_genres s
	ON g.id = s.genre_id
	INNER JOIN tv_shows AS t
	ON s.show_id = t.id
	WHERE t.title = "Dexter")
ORDER BY g.`name`;
