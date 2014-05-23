import subprocess

from dir_util import current_directory

status_codes = {
    '??': 'untracked',
    'M': 'modified',
    'D': 'deleted',
    }

def git_status(repo_path='.'):
    with current_directory(repo_path):
        proc = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
    status_output = proc.stdout.read().decode('utf8')
    file_status = {}
    for line in status_output.split('\n'):
        line = line.strip()
        if line:
            status_code, filename = line.split(' ', 1)
            status = status_codes[status_code]
            file_status[filename] = status
    return file_status


def git_current_branch(repo_path='.'):
    with current_directory(repo_path):
        proc = subprocess.Popen(['git', 'branch'], stdout=subprocess.PIPE)

    for line in proc.stdout.readlines():
        line = line.decode('utf8')
        if line[0] == '*':
            return line[2:].strip()

    raise ValueError('git branch did not return a branch name')
