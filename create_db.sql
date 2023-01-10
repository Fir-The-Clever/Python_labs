drop database if exists service_db;
drop role if exists lab4;

create user lab4;
alter user lab4 with encrypted password 'lab4';
alter role lab4 superuser;
create database service_db owner lab4;

\connect service_db;

DROP TABLE if exists service.users;


CREATE TABLE service.users (id SERIAL NOT NULL, full_name VARCHAR NOT NULL, login VARCHAR NOT NULL, password VARCHAR NOT NULL);
INSERT INTO service.users (full_name, login, password) VALUES ('Ivan Proba','Fir', '12345'); 

INSERT INTO service.users (full_name, login, password) VALUES ('Peter Parker','Spidey', '111'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Tony Stark','Stark', '222'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Clark Kent','Super', '333'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Diana Prince','Wonder', '444'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Kamala Khan','Marvel', '555'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Billy Batcon','Shazam', '666'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Bruce Wayne','Bat', '777'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Matt Merdock','Devil', '888'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Barry Allen','Flash', '999'); 
INSERT INTO service.users (full_name, login, password) VALUES ('Doctor','Doctor', '000'); 

SELECT * FROM service.users;
