from pathlib import Path
from pytest_console_scripts import ScriptRunner
import os
import pytest
import shlex
import subprocess


BIN_STUBS = Path(__file__).parent.joinpath('bin_stubs')


@pytest.fixture(scope='session', autouse=True)
def gitrepo(tmpdir_factory):
    folder = tmpdir_factory.mktemp("data")
    os.chdir(folder)

    def run(cmd):
        return subprocess.check_call(shlex.split(cmd), cwd=folder)

    run('git init')
    run('git remote add origin git@github.com:4teamwork/ftw.deploy.test.git')
    run('git remote add prod example.com:/apps/01-prod')
    run('git remote add test example.com:/apps/02-test')

    run(f'ln -s {BIN_STUBS} bin')
    os.environ['PATH'] = ':'.join((str(BIN_STUBS), os.environ['PATH']))
    return gitrepo


@pytest.fixture(scope='class', autouse=True)
def script_runner(request):
    request.cls.script_runner = ScriptRunner('subprocess', gitrepo).run
