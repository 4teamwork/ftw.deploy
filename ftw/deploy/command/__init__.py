import argparse
import os
import sys

from pkg_resources import get_distribution


VERSION = get_distribution('ftw.deploy').version


class DeployCommand(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(os.path.basename(sys.argv[0]))
        self.parser.add_argument('--version', action='version', version=VERSION)

    def __call__(self):
        self.parser.parse_args()


def main():
    DeployCommand()()
