CREATE TABLE IF NOT EXISTS vote_employees(
    id serial primary key,
    external_id int,
    employee_id int references employees(id)
);