-- a script that prepares a MySQL server for the project
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- granting previleges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- revoking all privileges
REVOKE ALL PRIVILEGES ON *.* FROM 'hbnb_dev'@'localhost';

-- grant select privelege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flushing privileges
FLUSH PRIVILEGES;
