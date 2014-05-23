from collections import Counter

from blessings import Terminal

from git_utils import git_status, git_current_branch
from dir_util import shrink_path_for_display

t = Terminal()


def process_status_command(args, config, config_file):
    max_repo_len = max([len(x) for x in config['repos']])

    for repo in config['repos']:
        status = git_status(repo)
        current_branch = git_current_branch(repo)

        status_type_counts = Counter(status.values())
        modified_or_deleted_count = status_type_counts['modified'] + status_type_counts['deleted']
        untracked_count = status_type_counts['untracked']

        if modified_or_deleted_count:
            status_text = t.red('%s modified' % modified_or_deleted_count)
        elif untracked_count:
            status_text = t.yellow('%s untracked' % untracked_count)
        else:
            status_text = t.green('Clean')

        print(shrink_path_for_display(repo), ' ' * (max_repo_len - len(repo)), status_text)
