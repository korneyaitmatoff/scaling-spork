CREATE TABLE IF NOT EXISTS employees(
    id serial primary key,
    name varchar,
    login varchar,
    password varchar,
    created_at timestamp default now(),
    changed_at timestamp default now()
);