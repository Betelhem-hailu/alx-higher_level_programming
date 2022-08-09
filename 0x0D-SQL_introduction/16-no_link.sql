-- Is a script that lists all records of the table second_table in my MYSQL server
-- query used to omit no value record
SELECT name, score FROM second_table WHERE name = "%like%" ORDER BY score DESC;