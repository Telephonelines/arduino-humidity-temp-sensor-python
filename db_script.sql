DROP DATABASE IF EXISTS temperaturedb;
CREATE DATABASE temperaturedb;
USE temperaturedb;

CREATE TABLE readings (
	id INT AUTO_INCREMENT PRIMARY KEY,
	date DATETIME DEFAULT NOW(),
	humidity FLOAT, 
	temperature FLOAT
);

SELECT * FROM readings;