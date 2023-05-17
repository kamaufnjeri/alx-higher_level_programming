-- join two tables and read title and gnere_id
SELECT s.title, tg.genre_id
FROM tv_shows s LEFT OUTER JOIN tv_show_genres tg
ON s.id = tg.show_id
ORDER BY s.title, tg.genre_id;
