from ..templates import TEMPLATES


DOCS = """
DESCRIPTION:
    The purpose of the "init" command is to add deployment scripts to the
    repository so that the repository is ready for push deployment.

EXAMPLES:
    $ bin/upgrade init plone
    $ bin/upgrade init django
"""


def setup_argparser(commands):
    command = commands.add_parser('init',
                                  help='Add deployment scripts to this repository.',
                                  description=DOCS)
    command.set_defaults(func=init_command)

    command.add_argument('template',
                         choices=TEMPLATES.keys(),
                         help='The type of project, used for selecting the right scripts.',
                         default=None)


def init_command(args):
    print(f'Installing {args.template} deployment scripts.')
    TEMPLATES[args.template]().install()
