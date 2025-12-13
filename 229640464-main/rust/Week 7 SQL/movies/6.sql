-- In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
SELECT AVG(rank.rating) FROM movies films JOIN ratings rank ON films.id = rank.movie_id WHERE films.year = 2012;
