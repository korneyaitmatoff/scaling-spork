CREATE OR REPLACE FUNCTION
create_student
(
    name varchar,
    group_code varchar,
    is_resident bool,
    passport_data jsonb,
    inn varchar default ''
) RETURNS BOOLEAN AS
$$
BEGIN
    IF is_resident IS TRUE AND inn = '' THEN
        RETURN FALSE;
    ELSE
        CALL add_student(
            name => name,
            group_code => group_code,
            is_resident => is_resident,
            passport_data => passport_data,
            inn => inn
        );

        RETURN TRUE;
    END IF;
END;
$$
    LANGUAGE 'plpgsql';