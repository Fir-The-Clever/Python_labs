drop database if exists lab3_db;
drop role if exists lab3;

create user lab3 ;
alter user lab3 with encrypted password 'lab3';
alter role lab3 superuser;
create database lab3_db owner lab3;

\connect lab3_db;

DROP TABLE if exists department;
CREATE TABLE department (dep_id SERIAL PRIMARY KEY, dep_name varchar NOT NULL, dean varchar NOT NULL);
INSERT INTO department (dep_name, dean) VALUES ('IU5', 'Ivan Proba');
INSERT INTO department (dep_name, dean) VALUES ('IU7', 'Vadim Allmight');

DROP TABLE if exists student_group;
CREATE TABLE student_group (gr_id SERIAL PRIMARY KEY, gr_name varchar NOT NULL, dep_id int REFERENCES department(dep_id));
INSERT INTO student_group (gr_name, dep_id) VALUES ('IU5-1', 1);
INSERT INTO student_group (gr_name, dep_id) VALUES ('IU5-2', 1);
INSERT INTO student_group (gr_name, dep_id) VALUES ('IU7-3b', 2);
INSERT INTO student_group (gr_name, dep_id) VALUES ('IU7-4b', 2);

DROP TABLE if exists student;
CREATE TABLE student (st_id SERIAL PRIMARY KEY, st_name varchar NOT NULL, address varchar NOT NULL, gr_id int REFERENCES student_group(gr_id));
INSERT INTO student (st_name, address, gr_id) VALUES ('Tony Stark', 'Moscow', 1);
INSERT INTO student (st_name, address, gr_id) VALUES ('Steve Rogers', 'Moscow', 1);
INSERT INTO student (st_name, address, gr_id) VALUES ('Peter Parker', 'Moscow', 1);
INSERT INTO student (st_name, address, gr_id) VALUES ('Charles Xavier', 'Moscow', 1);
INSERT INTO student (st_name, address, gr_id) VALUES ('Clint Barton', 'Moscow', 1);

INSERT INTO student (st_name, address, gr_id) VALUES ('Clark Kent', 'SPb', 2);
INSERT INTO student (st_name, address, gr_id) VALUES ('Diana Prince', 'SPb', 2);
INSERT INTO student (st_name, address, gr_id) VALUES ('Barry Allen', 'SPb', 2);
INSERT INTO student (st_name, address, gr_id) VALUES ('Wally West', 'SPb', 2);
INSERT INTO student (st_name, address, gr_id) VALUES ('Billy Batson', 'SPb', 2);

SELECT * FROM student WHERE gr_id = 2;
