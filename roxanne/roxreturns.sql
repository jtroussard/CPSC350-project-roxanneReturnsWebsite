DROP DATABASE IF EXISTS roxreturns;


CREATE DATABASE roxreturns;

 \c roxreturns;

 --
-- Table structure for table City
--

DROP TABLE IF EXISTS Members;


CREATE TABLE Members (member_id serial PRIMARY KEY, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL, email varchar(50) NOT NULL, YEAR int, model varchar(30) DEFAULT '');

 --
-- Dumping data for table City
--
-- ORDER BY:  ID

INSERT INTO Members (first_name, last_name, email, YEAR, model)
VALUES ( 'Jacques',
         'Troussard',
         'jacques@some-email.com',
         1971,
         'Pontiac GTO (hardtop)');


INSERT INTO members
VALUES (DEFAULT,
        'Michael',
        'Hendrey',
        'mikey@some-email.com',
        1970,
        'Chevrolet Chevelle');


INSERT INTO members
VALUES (DEFAULT,
        'Zelco',
        'Cecich',
        'zel-cab@email.com',
        1955,
        'Chevrolet 3100s');


INSERT INTO members
VALUES (DEFAULT,
        'Grant',
        'Thornton',
        'punkrocker@email.com',
        1953,
        'Chevrolet 210 Wagon');


INSERT INTO members
VALUES (DEFAULT,
        'Christine',
        'Kappa',
        'racer_girl@email.com',
        1967,
        'Chevrolet Camaro');


INSERT INTO members
VALUES (DEFAULT,
        'Emily',
        'Romanova',
        'eroma@email.com',
        1965,
        'Pontiac GTO (hardtop)');


INSERT INTO members
VALUES (DEFAULT,
        'Xaiver',
        'Zander',
        'triplex@staremail.com',
        1967,
        'Pontiac GTO (hardtop)');