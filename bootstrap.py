from src.dependencies import db_engine

def get_script_from_file(script_name: str) -> str:
    with open(f"sql/{script_name}", "r") as f:
        return f.read()

if __name__ == "__main__":
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_employees.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_students.sql"))

    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_vote_employees.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_vote_students.sql"))

    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_incoming_request.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_votes.sql"))
    db_engine.execute_and_commit(statement=get_script_from_file(script_name="create_table_protocol.sql"))
