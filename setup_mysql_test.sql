-- a script that prepares a MySQL server for the project
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- granting previleges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privelege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flushing privileges
FLUSH PRIVILEGES;
