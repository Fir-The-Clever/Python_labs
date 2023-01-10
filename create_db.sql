drop database if exists schedule_db;
drop role if exists lab7;

create user lab7;
alter user lab7 with encrypted password 'lab7';
alter role lab7 superuser;
create database schedule_db owner lab7;

\connect schedule_db;

DROP TABLE if exists subject;
DROP TABLE if exists timetable;
DROP TABLE if exists teacher;


CREATE TABLE subject (sub_id SERIAL PRIMARY KEY, title VARCHAR NOT NULL);
INSERT INTO subject (title) VALUES ('МХК');
INSERT INTO subject (title) VALUES ('Программирование');
INSERT INTO subject (title) VALUES ('ИИ');
INSERT INTO subject (title) VALUES ('Физика');
INSERT INTO subject (title) VALUES ('Литература');

select * from subject;

CREATE TABLE teacher (teacher_id SERIAL PRIMARY KEY, full_name VARCHAR NOT NULL, sub_id int REFERENCES subject(sub_id));
INSERT INTO teacher (full_name, sub_id) VALUES ('Иванов Иван Иванович', 1); 
INSERT INTO teacher (full_name, sub_id) VALUES ('Белодедов Дед Дедович', 2);
INSERT INTO teacher (full_name, sub_id) VALUES ('Белодедов Дед Дедович', 5);
INSERT INTO teacher (full_name, sub_id) VALUES ('Афанасьев Афанасий Афанасьевич', 3); 
INSERT INTO teacher (full_name, sub_id) VALUES ('Постников Дед Иванович', 4); 

CREATE TABLE timetable (t_id SERIAL PRIMARY KEY, day VARCHAR NOT NULL, sub_id int REFERENCES subject(sub_id), room VARCHAR NOT NULL, start VARCHAR NOT NULL);
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Понедельник', 1, '627', '9:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Понедельник', 2, '7', '11:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Понедельник', 3, '4', '13:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Вторник', 4, '627', '9:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Вторник', 4, '627', '11:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Вторник', 5, '14', '17:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Вторник', 5, '14', '19:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Среда', 3, '627', '17:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Пятница', 1, '33', '12:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Пятница', 4, 'Э55', '17:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Суббота', 2, '55', '15:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Суббота', 3, '67', '17:00');
INSERT INTO timetable (day, sub_id, room, start) VALUES ('Суббота', 4, '57', '19:00');

SELECT * FROM timetable 
JOIN subject on timetable.sub_id = subject.sub_id
JOIN teacher on teacher.sub_id = subject.sub_id







