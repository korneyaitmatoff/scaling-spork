CREATE TABLE IF NOT EXISTS vote_employees(
    id serial primary key,
    vote_id int references votes(id),
    protocol_id int references protocols(id),
    employee_id int references employees(id)
);