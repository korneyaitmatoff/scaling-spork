CREATE OR REPLACE PROCEDURE
add_student
(
    name varchar,
    group_code varchar,
    inn varchar,
    is_resident bool,
    passport_data jsonb
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO students(name, group_code, inn, is_resident, passport_data)
    VALUES (name, group_code, inn, is_resident, passport_data);
END;