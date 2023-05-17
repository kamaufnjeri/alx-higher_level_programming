-- list name and genre and sort by title and genre
SELECT s.title, g.name
FROM tv_shows s LEFT OUTER JOIN tv_show_genres sg
ON s.id = sg.show_id
LEFT OUTER JOIN tv_genres g
ON g.id = sg.genre_id
ORDER BY s.title, g.name;
