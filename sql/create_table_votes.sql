CREATE TABLE IF NOT EXISTS votes(
    id serial primary key,
    maintainer_id int references employees(id),
    votes_json jsonb default null,
    created_at timestamp default now(),
    changed_at timestamp default now()
);