-- Write an SQL query to add the following people in the people table --
INSERT OR IGNORE INTO people (id, name, birth)
VALUES (191, 'Ewan Gordon McGregor', 1971);

INSERT OR IGNORE INTO people (id, name, birth)
VALUES  (204, 'Natalie Portman', 1981);

INSERT OR IGNORE INTO people (id, name, birth)
VALUES  (159789, 'Hayden Christensen', 1981);

INSERT OR IGNORE INTO people (id, name, birth)
VALUES (184, 'George Lucas', 1944);

-- Check of the existence of people added --

SELECT * FROM people WHERE id = 191;
SELECT * FROM people WHERE id = 204;
SELECT * FROM people WHERE id = 159789;
SELECT * FROM people WHERE id = 184;
