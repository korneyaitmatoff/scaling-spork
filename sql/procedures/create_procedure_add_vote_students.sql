CREATE OR REPLACE PROCEDURE
add_vote_students
(
    student_id int,
    vote_id int,
    protocol_id int
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO vote_students(student_id, vote_id, protocol_id)
    VALUES (student_id, vote_id, protocol_id);
END;
