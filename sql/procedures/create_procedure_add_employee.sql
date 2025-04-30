CREATE OR REPLACE PROCEDURE
add_employee(
    name varchar,
    login varchar,
    password varchar
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO employees(name, login, password) VALUES (name, login, MD5(password));
END;