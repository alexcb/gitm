from blessings import Terminal

from dir_util import shrink_path_for_display

t = Terminal()

def process_list_command(args, config, config_file):
    repos = config['repos']
    if not repos:
        print('No registered repositories, use the discover command to add repositories.')
        return

    print('%s registered repositories:\n%s' % (
        len(repos),
        '\n'.join([t.green('  %s') % shrink_path_for_display(x) for x in repos])),
        )
