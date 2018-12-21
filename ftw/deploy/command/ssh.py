import argparse

from ..gitsupport import get_remote_names
from ..gitsupport import get_ssh_string_of_remote
from ..sshsupport import ssh_connect


DOCS = """
DESCRIPTION:
    The "ssh" command establieshes an ssh connection to the deploymennt
    and cd's into the correct directory.

EXAMPLES:
    $ bin/upgrade ssh prod
"""


def setup_argparser(commands):
    command = commands.add_parser('ssh',
                                  help='Connect with to the deployment with ssh.',
                                  description=DOCS)
    command.set_defaults(func=ssh_command)

    command.add_argument('remote',
                         choices=get_remote_names(),
                         help='The git remote to ssh to.',
                         default=None)

    command.add_argument('--user', '-u',
                         help='Change the ssh user.',
                         default=None)

    command.add_argument('ssh_options', nargs=argparse.REMAINDER)


def ssh_command(args):
    remote_ssh_string = get_ssh_string_of_remote(args.remote)
    ssh_connect(remote_ssh_string, args.ssh_options, args.user)
