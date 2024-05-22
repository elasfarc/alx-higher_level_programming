--script that creates a table called first_table in the current database in your MySQL server.

--first_table description:
--id INT
--name VARCHAR(256)

-- create the table first_table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
    );
