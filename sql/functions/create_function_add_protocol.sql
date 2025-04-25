CREATE OR REPLACE FUNCTION
add_protocol(
    number varchar,
    maintainer_id int ,
    vote_id int,
    budget_amount int,
    vote_json jsonb
) RETURNS VOID AS
$$
BEGIN
    INSERT INTO protocols(number, maintainer_id, vote_id, budget_amount, vote_json)
    VALUES(number, maintainer_id, vote_id, budget_amount, vote_json);
END
$$
    LANGUAGE 'plpgsql';