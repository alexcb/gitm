#!/bin/python3.4
import sys
import os
import subprocess

from blessings import Terminal

from commands.discover import process_discover_command
from commands.list import process_list_command
from commands.status import process_status_command
from commands.branch import process_branch_command

from arg_parser import get_args
from user_conf import load_config_or_default, save_config
from dir_util import current_directory


t = Terminal()

def process_execute_command(args, config):
    for repo in config['repos']:
        print('Running in: %s' % t.cyan(repo))
        with current_directory(repo):
            try:
                subprocess.check_call(args.exec)
            except subprocess.CalledProcessError as e:
                print(t.red('Error: user supplied command returned error code: %s' % e.returncode))
                sys.exit(1)
            except FileNotFoundError as e:
                print(t.red('Error: user supplied command not found: %s' % e))
                sys.exit(1)
        print('')


def main():
    args = get_args()

    config_file = '~/.gitm'
    config_file = os.path.expanduser(config_file)
    try:
        config = load_config_or_default(config_file)
    except FileNotFoundError:
        config = {}

    if args.exec and args.cmd:
        print('Only a command or external shell command can be specified at a time', file=sys.stderr)
        sys.exit(1)

    # Execute command across all repos
    if args.exec:
        process_execute_command(args, config)
        sys.exit(0)

    # Or process commands
    command_handlers = {
        'discover': process_discover_command,
        'list': process_list_command,
        'status': process_status_command,
        'branch': process_branch_command,
        }
    command = args.cmd or 'list'
    try:
        command_handler = command_handlers[command]
    except KeyError as e:
        print('Unknown command: %s' % e)
    else:
        command_handler(args, config, config_file)

if __name__ == '__main__':
    main()
