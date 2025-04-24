CREATE TABLE IF NOT EXISTS students(
    id serial primary key,
    name varchar,
    group_code varchar,
    inn varchar,
    is_resident bool,
    passport_data jsonb,
    created_at timestamp default now(),
    changed_at timestamp default now()
);