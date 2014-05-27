from blessings import Terminal

from gitm.dir_util import shrink_path_for_display
from gitm.tag_util import get_repos

t = Terminal()

def process_list_command(args, config, config_file):
    repos = get_repos(config, args.tag)
    if not repos:
        print('No registered repositories, use the discover command to add repositories.')
        return

    print('%s registered repositories%s:\n%s' % (
        len(repos),
        'with tag "%s"' % args.tag if args.tag else '',
        '\n'.join([t.green('  %s') % shrink_path_for_display(x) for x in repos])),
        )
