from pathlib import Path

def get_input_path_str(module_path):
    return str(Path(module_path).parent / 'input.txt')
