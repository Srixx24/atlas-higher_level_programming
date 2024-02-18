-- Lists all the cities of California
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states AND WHERE name = 'California')
ORDER BY id ASC;
