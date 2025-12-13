-- Write an SQL query linking George Lucas as director for all Star Wars films --
SELECT title, 'George Lucas' AS director
FROM movies
WHERE title LIKE '%Star Wars%';
