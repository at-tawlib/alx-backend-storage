-- Create table users with these requirements -- id (integer, never null, autoincrement and primary key)
-- email (string, never null and unique)
-- name (string)
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);