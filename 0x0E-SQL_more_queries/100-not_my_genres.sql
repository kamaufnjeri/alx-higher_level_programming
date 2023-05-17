SELECT DISTINCT t.name
FROM tv_genres t INNER JOIN tv_show_genres tg
ON t.id = tg.genre_id
INNER JOIN tv_genres s
ON s.id = tg.show_id
WHERE t.name NOT IN (
	SELECT g.name
	FROM tv_genres g
	INNER JOIN tv_show_genres tg
	ON g.id = tg.genre_id 
	INNER JOIN tv_shows s
	ON s.id = tg.show_id
	WHERE s.title = 'Dexter')
ORDER BY t.name;
