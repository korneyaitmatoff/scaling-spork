CREATE OR REPLACE PROCEDURE
add_vote_employees
(
    vote_id int,
    protocol_id int,
    employee_id int
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO vote_employees(vote_id, protocol_id, employee_id)
    VALUES (vote_id, protocol_id, employee_id);
END;