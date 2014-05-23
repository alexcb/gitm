import os
import itertools

from blessings import Terminal

from discovery import discover_git_repos
from user_conf import save_config
from dir_util import shrink_path_for_display

t = Terminal()

def process_discover_command(args, config, config_file):
    paths_to_search = args.cmd_args or ['.']

    discovered_repos = [os.path.abspath(x)
        for x in itertools.chain(*[discover_git_repos(x) for x in paths_to_search])]
    new_repos = [x for x in discovered_repos if x not in config['repos']]
    existing_repos = [x for x in discovered_repos if x in config['repos']]

    if new_repos:
        print('Adding new repos:\n%s' % '\n'.join([
            t.green('  %s') % shrink_path_for_display(x) for x in new_repos]))
        print('%s new git repositories found' % len(new_repos))
        try:
            config['repos'].extend(new_repos)
        except KeyError:
            config['repos'] = new_repos
        save_config(config, config_file)
    else:
        print('No new git repositories found (%s existing repositories discovered)' % (
            len(discovered_repos,)))
