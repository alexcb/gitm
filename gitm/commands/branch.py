from git_utils import git_current_branch
from dir_util import shrink_path_for_display
from blessings import Terminal
t = Terminal()

from collections import Counter

def process_branch_command(args, config, config_file):
    max_repo_len = max([len(x) for x in config['repos']])

    for repo in config['repos']:
        current_branch = git_current_branch(repo)

        print(shrink_path_for_display(repo), ' ' * (max_repo_len - len(repo)), t.green(current_branch))

