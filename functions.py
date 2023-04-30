def get_todos(file_path="todos.txt"):
    """Reads a file and returns saved to-dos
    as a list."""
    with open(file_path, "r") as file_local:
        local_todos = file_local.readlines()
    return local_todos


def write_todos(todos_arg, file_path="todos.txt"):
    """Gets the updated list of to-dos and
    saves it into a file for later use."""
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_arg)
