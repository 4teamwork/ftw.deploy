import unittest
from pathlib import Path

from ..sshsupport import SCRIPTS_DIR
from .conftest import BIN_STUBS


FTW_DEPLOY_ROOT = Path(__file__).joinpath('..', '..', '..', '..').resolve()


class TestCase(unittest.TestCase):

    def testTearDown(self):
        self.purge_executed_commands()

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
