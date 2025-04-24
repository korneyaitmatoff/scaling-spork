CREATE TABLE IF NOT EXISTS protocols(
    id serial primary key,
    number varchar,
    doc_date timestamp default now(),
    maintainer_id int references employees(id),
    vote_id int references votes(id),
    budget_amount int,
    vote_json jsonb default null,
    created_at timestamp default now(),
    changed_at timestamp default now()
);