import os
from contextlib import contextmanager

@contextmanager
def current_directory(dir_path):
    original_dir = os.getcwd()
    try:
        os.chdir(dir_path)
        yield
    finally:
        os.chdir(original_dir)

def shrink_path_for_display(path):
    user_path = os.path.expanduser('~')
    if path.startswith(user_path):
        path = '~' + path[len(user_path):]
    return path
