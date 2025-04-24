CREATE TABLE IF NOT EXISTS incoming_requests(
    id serial primary key,
    student int references students(id),
    reason varchar,
    study_kind varchar,
    name varchar,
    is_commerce bool,
    faculty varchar,
    course int,
    group_code varchar,
    contact varchar,
    doc_date timestamp default now(),
    created_at timestamp default now(),
    changed_at timestamp default now()
);