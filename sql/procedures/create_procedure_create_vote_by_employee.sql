CREATE OR REPLACE PROCEDURE
create_vote_by_employee
(
    employee_id int,
    vote_id int,
    student_id int
)
LANGUAGE plpgsql AS
$$
DECLARE is_vote_exists BOOLEAN;
DECLARE is_employee_exists BOOLEAN;
DECLARE is_student_exists BOOLEAN;
DECLARE is_vote_part_exists BOOLEAN;
BEGIN
    SELECT count(*) >= 1 INTO is_vote_part_exists FROM
    vote_employees ve where
    ve.vote_id = vote_id
    and ve.employee_id = employee_id;


    IF is_vote_exists IS TRUE THEN
        RAISE EXCEPTION 'Current employee already vote for this student';
    ELSE
        SELECT count(*) >= 1 INTO is_vote_exists FROM votes v WHERE v.id = vote_id;
        SELECT count(*) >= 1 INTO is_employee_exists FROM employees e WHERE e.id = employee_id;
        SELECT count(*) >= 1 INTO is_student_exists FROM students s WHERE s.id = student_id;

        IF (is_vote_exists and is_employee_exists and is_student_exists) IS FALSE THEN
            RAISE EXCEPTION 'There are dont exists vote, student, employee';
        ELSE
            INSERT INTO vote_employees(vote_id, protocol_id, employee_id)
            VALUES (vote_id, protocol_id, employee_id);
        END IF;
    END IF;
END;
$$
