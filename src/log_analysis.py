def load_logs(filepath: str):
    with open(filepath, 'r') as file:
        return file.readlines()