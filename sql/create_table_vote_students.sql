CREATE TABLE IF NOT EXISTS vote_students(
    id serial primary key,
    student_id int references students(id),
    vote_id int references votes(id),
    protocol_id int references protocols(id)
);