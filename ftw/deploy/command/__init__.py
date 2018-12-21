import argparse
import os
import sys

from . import help
from . import init
from . import rerun
from . import setup
from . import update
from .. import VERSION
from .formatter import FlexiFormatter


class DeployArgumentParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        kwargs['formatter_class'] = FlexiFormatter
        super().__init__(*args, **kwargs)


class DeployCommand(object):

    def __init__(self):
        self.parser = DeployArgumentParser(os.path.basename(sys.argv[0]))
        self.parser.add_argument('--version', action='version', version=VERSION)
        commands = self.parser.add_subparsers(help='Command', dest='command')

        init.setup_argparser(commands)
        rerun.setup_argparser(commands)
        setup.setup_argparser(commands)
        update.setup_argparser(commands)

        help.setup_argparser(commands)

    def __call__(self):
        args = self.parser.parse_args()
        setattr(args, 'parser', self.parser)
        if args.command:
            args.func(args)
        else:
            self.parser.print_help()


def main():
    DeployCommand()()
