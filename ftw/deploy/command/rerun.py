from ..gitsupport import get_remote_names
from ..gitsupport import get_ssh_string_of_remote
from ..sshsupport import rerun_last_deployment


DOCS = """
DESCRIPTION:
    The "rerun" comman runs the last deployment again.
    It uses "git rev-parse HEAD@{1}" in order to determine the previous
    deployment state.

EXAMPLES:
    $ bin/upgrade rerun prod
"""


def setup_argparser(commands):
    command = commands.add_parser('rerun',
                                  help='Rerun the last deployment.',
                                  description=DOCS)
    command.set_defaults(func=rerun_command)

    command.add_argument('remote',
                         choices=get_remote_names(),
                         help='The git remote to rerun.',
                         default=None)


def rerun_command(args):
    remote_ssh_string = get_ssh_string_of_remote(args.remote)
    rerun_last_deployment(remote_ssh_string)
