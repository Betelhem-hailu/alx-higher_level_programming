-- Is a script that lists the number of records with the same score int the second_table in my MYSQL server
-- query used to count
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;