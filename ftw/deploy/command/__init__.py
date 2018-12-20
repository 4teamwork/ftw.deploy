import argparse
import os
import sys

from pkg_resources import get_distribution

from . import help
from . import init
from . import setup
from .formatter import FlexiFormatter


VERSION = get_distribution('ftw.deploy').version


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
        setup.setup_argparser(commands)

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
