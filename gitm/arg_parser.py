import argparse
import sys
from textwrap import dedent

def split_command_from_args(argv):
    # argparse did not work because I wanted functionality such as:
    # gitm -- echo foo
    #   to execute the passed command across all git repos
    #   with an option to use a group:
    #     gitm -g work -- echo foo
    # or, to run the internal commands:
    # gitm <cmd>

    if '--' in argv:
        end_arg_pos = argv.index('--')
        args_to_parse = argv[:end_arg_pos]
        exec_command = argv[end_arg_pos+1:]
    else:
        end_arg_pos = len(argv)
        args_to_parse = argv[:]
        exec_command = None

    return args_to_parse, exec_command


def get_arg_parser():
    parser = argparse.ArgumentParser(
        description='Git\'em - multiple git repo manager', 
        add_help=False,
        usage='[-h] [--group GROUP] [cmd] [-- [EXEC]]',
        )
    parser.add_argument('cmd', nargs='?')
    parser.add_argument('cmd_args', nargs='*')
    #parser.add_argument('dir', nargs='?')
    #parser.add_argument('-g', '--group')
    parser.add_argument('-h', '--help', action='store_true', default=False)
    return parser


def display_help():
    print(dedent('''\
    Usage: gitm [--help] <cmd> [<cmd arguments> ...] [-- <external cmd>]

    options:
        --help          display this help screen

    cmd:
        list            displays all registered git repos
        status          display a condensed status of any modification across all git repos
        branch          display the current branch across all git repos
        discover <path> recursively searches the path for any new git repos to register

    external cmd:
        Runs the external shell command for each git repo.
        Only one of cmd or external cmd can be specified at a single time.

        Example:
        gitm -- pwd

            Running in: /home/alexcb/git/other_repo
            /home/alexcb/git/other_repo
            
            Running in: /home/alexcb/git/gitm
            /home/alexcb/git/gitm
    '''))

def display_help_if_required_and_quit(args):
    if args.help:
        display_help()
        sys.exit(0)

def get_args():
    args_to_parse, exec_command = split_command_from_args(sys.argv[1:])
    
    parser = get_arg_parser()
    args = parser.parse_args(args_to_parse)
    display_help_if_required_and_quit(args)
    
    args.exec = exec_command
    return args
