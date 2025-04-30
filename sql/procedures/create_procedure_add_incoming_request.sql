CREATE OR REPLACE PROCEDURE
add_incoming_request(
    student_id int ,
    reason varchar,
    study_kind varchar,
    name varchar,
    is_commerce bool,
    faculty varchar,
    course int,
    group_code varchar,
    contact varchar
)
LANGUAGE SQL
BEGIN ATOMIC
    INSERT INTO incoming_requests(student_id, reason, study_kind, name, is_commerce, faculty,
    course, group_code, contact) VALUES (student_id, reason, study_kind, name, is_commerce,
    faculty, course, group_code, contact);
END;