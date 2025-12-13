-- Write an SQL query to add the following movies in the movies table --
INSERT INTO movies (title)
VALUES
     ('80684 Star Wars: Episode V - The Empire Strikes Back 1980'),
     ('86190 Star Wars: Episode VI - Return of the Jedi 1983'),
     ('120915 Star Wars: Episode I - The Phantom Menace 1999'),
     ('121765 Star Wars: Episode II - Attack of the Clones 2002'),
     ('121766 Star Wars: Episode III - Revenge of the Sith 2005');

-- Check of the movies if succesfully added --
SELECT * FROM movies WHERE title LIKE 'Star Wars: Episode V - The Empire Strikes Back';
SELECT * FROM movies WHERE title LIKE 'Star Wars: Episode VI - Return of the Jedi';
SELECT * FROM movies WHERE title LIKE 'Star Wars: Episode I - The Phantom Menace';
SELECT * FROM movies WHERE title LIKE 'Star Wars: Episode II - Attack of the Clones';
SELECT * FROM movies WHERE title LIKE 'Star Wars: Episode III - Revenge of the Sith';

