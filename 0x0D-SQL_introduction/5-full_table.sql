-- Is a script that prints the full description of the table first_table from the database hbtn_0c_0 in my MYSQL server
-- query used to describe table
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='first_table';