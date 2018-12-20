import shlex
import subprocess
from pathlib import Path


SCRIPTS_DIR = Path(__file__).parent.joinpath('scripts')


def upload_post_receive_hook(remote_ssh_string):
    post_receive_script = SCRIPTS_DIR.joinpath('post-receive')
    command = f'scp {post_receive_script} {remote_ssh_string}/.git/hooks/post-receive'
    print(f'> {command}')
    subprocess.check_call(shlex.split(command))


def remote_execute(remote_ssh_string, command):
    user_host, directory = remote_ssh_string.split(':')
    command = f'ssh {user_host} "cd {directory} && {command}"'
    print(f'> {command}')
    subprocess.check_call(shlex.split(command))


def configure_remote_git_repository(remote_ssh_string):
    remote_execute(remote_ssh_string, 'git config --bool receive.denyNonFastForwards false')
    remote_execute(remote_ssh_string, 'git config receive.denyCurrentBranch ignore')
