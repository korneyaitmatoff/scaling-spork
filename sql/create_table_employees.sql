CREATE TABLE IF NOT EXISTS employees(
    id serial primary key,
    name varchar,
    login varchar unique,
    password varchar,
    created_at timestamp default now(),
    changed_at timestamp default now()
);