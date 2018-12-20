import argparse
import os
import pydoc
import sys


DOCS = """
DESCRIPTION:
    Display help information about the deploy commands.

EXAMPLES:
    $ bin/upgrade help
    $ bin/upgrade help create
"""


def setup_argparser(commands):
    command = commands.add_parser('help',
                                  help='Display help information.',
                                  description=DOCS)
    command.set_defaults(func=help_command)

    command.add_argument('command', nargs='?',
                         choices=get_commands(commands.container).keys(),
                         help='Command to describe.')


def help_command(args):
    commands = get_commands(args.parser)
    parser = commands.get(args.command, args.parser)
    if sys.stdout.isatty():
        if os.system('(less -R) 2>/dev/null') == 0:
            return pydoc.pipepager(parser.format_help(), cmd='less -R')
    else:
        print(parser.format_help())


def get_commands(parser):
    commands = {}
    for action in parser._actions:
        if not isinstance(action, argparse._SubParsersAction):
            continue
        commands.update(action.choices)
    return commands
