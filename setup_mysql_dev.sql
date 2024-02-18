-- Create a MySQL server for the project--
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Generate the hashed password
SET @hashed_password = PASSWORD('hbnb_dev_pwd');

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- Update the user's password in the mysql.user table
UPDATE mysql.user SET authentication_string = @hashed_password WHERE user = 'hbnb_dev' AND host = 'localhost';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
