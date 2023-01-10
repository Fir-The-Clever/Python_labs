

\connect schedule_db;



SELECT * FROM timetable 
JOIN subject on timetable.sub_id = subject.sub_id
JOIN teacher on teacher.sub_id = subject.sub_id WHERE timetable.day = 'Среда'







