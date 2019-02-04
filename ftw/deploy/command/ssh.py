import argparse
import os
import re
import sys

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

    command.add_argument('--tunnel', '-t',
                         help='Tunnel a bunch of deployment ports.',
                         action='store_true',
                         default=None)

    command.add_argument('ssh_options', nargs=argparse.REMAINDER)


def ssh_command(args):
    remote_ssh_string = get_ssh_string_of_remote(args.remote)
    options = args.ssh_options + get_tunnel_options(args)
    ssh_connect(remote_ssh_string, options, args.user)


def get_tunnel_options(args):
    if not args.tunnel:
        return []

    ssh_string = get_ssh_string_of_remote(args.remote)
    deployment_number = os.path.basename(ssh_string)[:2]
    if not re.match(r'^\d{2}$', deployment_number):
        print('ERROR: Could not find deployment number of remote.', file=sys.stderr)
        sys.exit(1)

    port_base = int(deployment_number) * 100

    ports = (
        10000,  # instance0
        10001,  # instance1
        10002,  # instance2
        10003,  # instance3
        10004,  # instance4
        10010,  # instancepub
        10030,  # solr
        10050,  # haproxy
    )

    return ['-L {0}:localhost:{0}'.format(port + port_base) for port in ports]
