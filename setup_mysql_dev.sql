-- Create a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Set password policy to low temporarily
SET GLOBAL validate_password.policy = LOW;

-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
