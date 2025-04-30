CREATE OR REPLACE PROCEDURE
add_protocol(
    number varchar,
    maintainer_id int ,
    vote_id int,
    budget_amount int,
    vote_json jsonb
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO protocols(number, maintainer_id, vote_id, budget_amount, vote_json)
    VALUES(number, maintainer_id, vote_id, budget_amount, vote_json);
END;