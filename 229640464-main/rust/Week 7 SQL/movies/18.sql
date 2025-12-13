-- Write an SQL query where all Star Wars films are rated 8.0 --
SELECT title, 8.0 AS rating
FROM movies
WHERE title LIKE '%Star Wars%';


