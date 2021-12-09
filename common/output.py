from pathlib import Path
from re import search
from common.turgid import LOGGER

def print_output(module_path, result):
    pattern = 'day(\d{2})/part(\d{2})'
    matches = search(pattern, str(Path(module_path)))
    day = matches.group(1)
    part = matches.group(2)
    print('Day {} Part {}, result: {}'.format(day, part, result))
