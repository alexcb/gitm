import os
import sys
from collections import Counter

from blessings import Terminal

from gitm.git_utils import git_current_branch
from gitm.dir_util import shrink_path_for_display
from gitm.user_conf import save_config

from gitm.dir_util import shrink_path_for_display

def process_tag_command(args, config, config_file):
    if not args.cmd_args or args.cmd_args[0] == 'list':
        for tag, repos in config['tags'].items():
            print('%s:\n%s' % (
                tag, '\n'.join(('  %s' % shrink_path_for_display(x) for x in repos))))
        sys.exit(0)
    
    if len(args.cmd_args) < 3 or args.cmd_args[0] not in ('add', 'rm'):
        print('command args must be: [add or rm] <tag> <repo> [<repo>, ...]', file=sys.stderr)
        sys.exit(1)

    operation = args.cmd_args[0]
    tag = args.cmd_args[1]
    repo_paths = args.cmd_args[2:]

    for repo_path in repo_paths:
        repo_path = os.path.abspath(os.path.expanduser(repo_path))
        if repo_path not in config['repos']:
            print('repo path "%s" not registered with gitm' % repo_path, file=sys.stderr)
            sys.exit(1)

        repos_in_tag = set(config['tags'].get(tag, []))
        if operation == 'add':
            repos_in_tag.add(repo_path)
        elif operation == 'rm':
            repos_in_tag.remove(repo_path)
        config['tags'][tag] = list(repos_in_tag)

    save_config(config, config_file)
        

#def get_key(t):
#    screen = curses.initscr()
#    screen.keypad(1)
#    key = screen.getch()
#    #curses.endwin()
#    return key
#
#def draw_menu(t, selected_line):
#    num_line_items = t.height - 3
#    assert num_line_items > 0
#
#    with t.location(0, 0):
#        print('Git Repo')
#    for i in range(num_line_items):
#        with t.location(0, 1 + i):
#            print('This is', t.underline('%s' % i))
#
#
#def process_edit_command(args, config, config_file):
#    t = Terminal()
#    max_items = 100
#    selected_line = 0
#    num_line_items = t.height - 3
#    assert num_line_items > 0
#
#    with t.fullscreen():
#        running = True
#        while running:
#            draw_menu(t, selected_line)
#            key = get_key(t)
#            #if key == ord('q'):
#            #    running = False
#            #if key == curses.KEY_UP:
#            #    selected_line = max(selected_line - 1, 0)
#            #if key == curses.KEY_DOWN:
#            #    selected_line = min(selected_line + 1, max_items)
#            #running = bool(key != ord('q'))
#            
#    #print('got key: %s %s' % (key, curses.KEY_UP))
