CREATE OR REPLACE PROCEDURE
add_vote(
    maintainer_id int,
    votes_json jsonb default null
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO votes(maintainer_id, votes_json) VALUES(maintainer_id, votes_json);
END;