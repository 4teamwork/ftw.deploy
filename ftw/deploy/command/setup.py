from ..gitsupport import get_remote_names
from ..gitsupport import get_ssh_string_of_remote
from ..sshsupport import configure_remote_git_repository
from ..sshsupport import upload_post_receive_hook


DOCS = """
DESCRIPTION:
    The purpose of the "setup" command is to configure a remote deployment git
    checkout so that it accepts pushes and executes the deployment script.

    The command adds a generic "post-receive" hook to the server-side git
    repository and configures the server-side git to allow receiving pushes on
    the current branch and supporting fast forward pushes.


PREREQUISITS:
    In order to use this command, the local git repository must already be
    configured with the target remote and it the necessary deployment scripts
    must be committed in the local repository.

EXAMPLES:
    $ bin/upgrade setup prod
"""


def setup_argparser(commands):
    command = commands.add_parser('setup',
                                  help='Setup hooks on a deployment git remote.',
                                  description=DOCS)
    command.set_defaults(func=setup_command)

    command.add_argument('remote',
                         choices=get_remote_names(),
                         help='The git remote to setup.',
                         default=None)


def setup_command(args):
    remote_ssh_string = get_ssh_string_of_remote(args.remote)
    upload_post_receive_hook(remote_ssh_string)
    configure_remote_git_repository(remote_ssh_string)
