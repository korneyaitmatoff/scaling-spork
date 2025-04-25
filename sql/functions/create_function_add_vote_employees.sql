CREATE OR REPLACE FUNCTION
add_vote_employees
(
    vote_id int,
    protocol_id int,
    employee_id int
) RETURNS VOID AS
$$
BEGIN
    INSERT INTO add_vote_employees(vote_id, protocol_id, employee_id)
    VALUES (vote_id, protocol_id, employee_id);
END
$$
    LANGUAGE 'plpgsql'