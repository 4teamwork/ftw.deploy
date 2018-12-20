import shlex
import subprocess


def get_remote_names():
    return tuple(map(lambda line: line.strip().decode('utf-8'),
                     subprocess.check_output(shlex.split('git remote')).strip().split()))


def get_ssh_string_of_remote(remote):
    return subprocess.check_output(
        shlex.split(f'git config --get remote.{remote}.url')
    ).strip().decode('utf-8')
