DROP DATABASE IF EXISTS roxreturns;


CREATE DATABASE roxreturns;

 \c roxreturns;

--
-- Table structure for table City
--

DROP TABLE IF EXISTS Members;


CREATE TABLE Members 
( 
	ID serial NOT NULL,
	first_name varchar(50) NOT NULL, 
	last_name varchar(50) NOT NULL, 
	email varchar(50) NOT NULL, 
	YEAR int, 
	model varchar(30) DEFAULT '', 
	PRIMARY KEY (ID)
);

--
-- Dumping data for table City
--
-- ORDER BY:  ID

INSERT INTO Members (first_name, last_name, email, year, model)
VALUES (
		'Jacques',
		'Troussard',
		'jacques@some-email.com',
		1971,
		'Pontiac GTO (hardtop)');



