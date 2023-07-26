-- 13. Number of shows by genre
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.name AS genre, COUNT(tg.name) AS number_of_shows
FROM tv_genres tg
RIGHT JOIN tv_show_genres tvg ON tg.id = tvg.genre_id
GROUP BY tg.name ORDER BY number_of_shows DESC;

