-- list all tv shows that are not comedies
SELECT DISTINCT s.title
FROM tv_shows s
LEFT OUTER JOIN tv_show_genres sg
ON s.id = sg.show_id
LEFT OUTER JOIN tv_genres g
ON g.id = sg.genre_id
WHERE s.title NOT IN (
	SELECT s.title
	FROM tv_shows s
	LEFT OUTER JOIN tv_show_genres sg
	ON s.id = sg.show_id
	LEFT OUTER JOIN tv_genres g
	ON g.id = sg.genre_id
	WHERE g.name = 'Comedy')
ORDER BY s.title;
