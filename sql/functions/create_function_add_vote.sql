CREATE OR REPLACE FUNCTION
add_vote(
    maintainer_id int,
    votes_json jsonb default null
) RETURNS VOID AS
$$
BEGIN
    INSERT INTO votes(maintainer_id, votes_json) VALUES(maintainer_id, votes_json);
END
$$
    LANGUAGE 'plpgsql';