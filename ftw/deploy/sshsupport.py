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
    command = ['ssh', user_host, f'cd {directory} && {command}']
    print('> {}'.format(' '.join(command)))
    subprocess.check_call(command)


def configure_remote_git_repository(remote_ssh_string):
    remote_execute(remote_ssh_string, 'git config --bool receive.denyNonFastForwards false')
    remote_execute(remote_ssh_string, 'git config receive.denyCurrentBranch ignore')


def rerun_last_deployment(remote_ssh_string):
    remote_execute(
        remote_ssh_string,
        "deploy/after_push `git rev-parse HEAD@{1} HEAD` | tee -a log/deploy.log")


def ssh_connect(remote_ssh_string, ssh_options, user):
    user_host, directory = remote_ssh_string.split(':')
    if user:
        if '@' in user_host:
            user_host = user_host.split('@', 1)[1]
        user_host = '@'.join((user, user_host))

    command = ['ssh'] + ssh_options + [user_host, '-t', f'cd {directory}; bash --login']
    print(f'connecting to:       {user_host}')
    print(f'change directory to: {directory}')
    print()
    print('> {}'.format(' '.join(command)))
    print()
    subprocess.check_call(command)
