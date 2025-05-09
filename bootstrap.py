from src.dependencies import db_engine


def get_script_from_file(script_name: str) -> str:
    with open(f"sql/{script_name}", "r") as f:
        return f.read()


if __name__ == "__main__":
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_employees.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_students.sql"))

    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_votes.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_protocol.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_incoming_request.sql"))

    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_vote_employees.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_vote_students.sql"))

    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_student.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_employee.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_incoming_request.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_vote.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_protocol.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_vote_students.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_add_vote_employees.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="procedures/create_procedure_create_vote_by_employee.sql")
    )

    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="functions/create_function_check_user_for_auth.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="functions/create_function_create_student.sql")
    )
    db_engine.execute_and_commit(
        statement=get_script_from_file(script_name="functions/create_function_create_incoming_request.sql")
    )
