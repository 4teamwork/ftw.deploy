import os
import unittest
from pathlib import Path
from shutil import rmtree

from ..sshsupport import SCRIPTS_DIR
from .conftest import BIN_STUBS


FTW_DEPLOY_ROOT = Path(__file__).joinpath('..', '..', '..', '..').resolve()


class TestCase(unittest.TestCase):

    def setUp(self):
        self.filesystem_before_testing = self.make_filesystem_snapshot()

    def testSetUp(self):
        self.filesystem_before_testing = self.make_filesystem_snapshot()

    def testTearDown(self):
        self.purge_executed_commands()
        self.reset_filesystem_to_snapshot(self.filesystem_before_testing)

    def tearDown(self):
        self.reset_filesystem_to_snapshot(self.filesystem_before_testing)

    def deploy(self, *arguments):
        """Run the deploy script with the given arguments.
        """
        return self.script_runner('deploy', *arguments)

    def get_executed_commands(self):
        log_file = Path('testing_stub_calls.log')
        if not log_file.exists():
            return []
        log = log_file.read_bytes().decode('utf-8')
        return self.replace_paths_in_output(log).splitlines()

    def replace_paths_in_output(self, output):
        output = output.replace(str(BIN_STUBS) + '/', '')
        output = output.replace(str(SCRIPTS_DIR), '{ftw.deploy/scripts}')
        output = output.replace(str(FTW_DEPLOY_ROOT), '{ftw.deploy}')
        return output

    def purge_executed_commands(self):
        log_file = Path('testing_stub_calls.log')
        if log_file.exists():
            log_file.unlink()

    def make_filesystem_snapshot(self):
        return (set(Path().glob('**/*'))
                - set([Path('.git')])
                - set(Path('.git').glob('**/*')))

    def reset_filesystem_to_snapshot(self, snapshot):
        for path in self.make_filesystem_snapshot() - snapshot:
            if path.is_dir():
                rmtree(path)
            if path.is_file() or os.path.lexists(path):
                path.unlink()
