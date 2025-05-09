CREATE OR REPLACE FUNCTION
create_incoming_request
(
    reason varchar,
    study_kind varchar,
    student_name varchar,
    is_commerce bool,
    faculty varchar,
    course int,
    student_group_code varchar,
    contact varchar
) RETURNS table (j json) AS
$$
DECLARE is_student_exists BOOLEAN;
DECLARE student_id INTEGER;
BEGIN
    SELECT COUNT(*) != 0 INTO is_student_exists
	FROM students s WHERE s.name = student_name AND s.group_code = student_group_code;

	IF is_student_exists is False THEN
	    RAISE EXCEPTION 'Student doesnt exists';
	ELSE
	    SELECT s.id INTO student_id FROM students s
	    WHERE s.name = student_name AND s.group_code = student_group_code;

	    CALL add_incoming_request(
	        student_id => student_id,
            reason => reason,
            study_kind => study_kind,
            name => student_name,
            is_commerce => is_commerce,
            faculty => faculty,
            course => course,
            group_code => student_group_code,
            contact => contact
	    );

	    RETURN QUERY SELECT json_build_object(
	        'id', student_id,
	        'name', student_name,
	        'reason', reason,
	        'study_kind', study_kind,
	        'is_commerce', is_commerce,
	        'faculty', faculty,
	        'course', course,
	        'group_code', student_group_code,
	        'contact', contact
	    );
	END IF;
END;
$$
    LANGUAGE 'plpgsql';
