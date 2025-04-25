CREATE OR REPLACE FUNCTION
add_vote_students
(
    student_id int,
    vote_id int,
    protocol_id int
) RETURNS VOID AS
$$
BEGIN
    INSERT INTO vote_students(student_id, vote_id, protocol_id)
    VALUES (student_id, vote_id, protocol_id);
END
$$
    LANGUAGE 'plpgsql';
