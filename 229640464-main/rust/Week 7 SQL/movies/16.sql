-- Write an SQL query linking the first three people of question 2 as stars of the film Revenge of the Sith --
SELECT title,
'Ewan Gordon McGregor, Natalie Portman, Hayden Christensen' AS stars
FROM movies
WHERE title = 'Star Wars: Episode III - Revenge of the Sith';



