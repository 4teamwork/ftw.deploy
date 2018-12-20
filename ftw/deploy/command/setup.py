from ..gitsupport import get_remote_names
from ..gitsupport import get_ssh_string_of_remote
from ..sshsupport import configure_remote_git_repository
from ..sshsupport import upload_post_receive_hook


def setup_argparser(commands):
    command = commands.add_parser('setup',
                                  help='Setup hooks on a deployment git remote.')
    command.set_defaults(func=setup_command)

    command.add_argument('remote',
                         choices=get_remote_names(),
                         help='The git remote to setup.',
                         default=None)


def setup_command(args):
    remote_ssh_string = get_ssh_string_of_remote(args.remote)
    upload_post_receive_hook(remote_ssh_string)
    configure_remote_git_repository(remote_ssh_string)
