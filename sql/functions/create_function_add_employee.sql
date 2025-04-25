CREATE OR REPLACE FUNCTION
add_employee(
    name varchar,
    login varchar,
    password varchar
) RETURNS VOID AS
$$
BEGIN
    INSERT INTO employees(name, login, password) VALUES (name, MD5(login), MD5(password));
END
$$
    LANGUAGE 'plpgsql';