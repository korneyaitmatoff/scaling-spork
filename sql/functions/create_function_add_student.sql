CREATE OR REPLACE FUNCTION add_student(
    name varchar,
    group_code varchar,
    inn varchar,
    is_resident bool,
    passport_data jsonb
    ) RETURNS VOID AS
    $$
    BEGIN
        INSERT INTO students(name, group_ode, inn, is_resident, passport_data)
        VALUES (name, group_ode, inn, is_resident, passport_data);
    END
    $$
        LANGUAGE "plpgsql";