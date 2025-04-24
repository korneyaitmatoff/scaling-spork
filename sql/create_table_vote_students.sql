CREATE TABLE IF NOT EXISTS vote_students(
    id serial primary key,
    external_id int,
    student_id int references students(id)
);