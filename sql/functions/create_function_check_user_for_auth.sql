CREATE OR REPLACE FUNCTION
is_correct_auth
(
    username varchar,
    passwd varchar
) RETURNS BOOLEAN AS
$$
DECLARE passed BOOLEAN;
BEGIN
    SELECT (count(*) = 1) INTO passed
    FROM employees as e where e.login = username and e.password = MD5(passwd);

    RETURN passed;
END;
$$ LANGUAGE 'plpgsql';