import sys
from operator import methodcaller

from ..templates import TEMPLATES


DOCS = """
DESCRIPTION:
    The purpose of the "update" command is to update deployment scripts.
    The update command needs certain files in the project
    for detecting the correct template.

EXAMPLES:
    $ bin/upgrade update
"""


def setup_argparser(commands):
    command = commands.add_parser('update',
                                  help='UIpdate deployment scripts in this repository.',
                                  description=DOCS)
    command.set_defaults(func=update_command)


def update_command(args):
    candidates = tuple(filter(methodcaller('is_applied_to_project'), TEMPLATES.values()))
    if len(candidates) == 0:
        print('ERROR: Could not detect template.', file=sys.stderr)
        sys.exit(1)
    elif len(candidates) > 1:
        print('ERROR: Conflicting template detection.', file=sys.stderr)
        sys.exit(1)
    else:
        template, = candidates
        print(f'Updating {template.name} deployment scripts.')
        template.update()
