-- Write an SQL query where the film Star Wars "Return of the Jedi" with a rating of 8.0 becomes a 10.0 --
SELECT movies.title, ratings.rating
FROM movies
JOIN ratings ON ratings.movie_id = movies.id
WHERE movies.title LIKE '%Star Wars: Episode VI - Return of the Jedi%';

