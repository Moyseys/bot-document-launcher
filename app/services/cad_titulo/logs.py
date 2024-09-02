import json
import os


def add_log(logs_file_path, log_entry):
    # Carregar logs existentes do arquivo JSON, se existir
    if os.path.exists(logs_file_path):
        with open(logs_file_path, 'r') as log_file:
            logs = json.load(log_file)
    else:
        logs = []

    logs.append(log_entry)

    # save os logs atualizados no arquivo JSON
    with open(logs_file_path, 'w') as log_file:
        json.dump(logs, log_file, indent=4)

def get_last_logged_line(logs_file_path):
    if not os.path.exists(logs_file_path):
        print("Log file does not exist.")
        return None

    with open(logs_file_path, 'r') as log_file:
        logs = json.load(log_file)
    
    if not logs:
        print("No logs found.")
        return None
    
    # A última entrada no log
    last_entry = logs[-1]
    
    # Retorna o valor da chave 'linha' se ela existir
    return last_entry.get("linha", None)