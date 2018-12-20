import re

from . import TestCase


class TestCommandRerun(TestCase):

    def test_requires_remote_name(self):
        ret = self.deploy('rerun')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'the following arguments are required: remote', ret.stderr)

    def test_existing_remotes_are_proposed_in_usage(self):
        ret = self.deploy('rerun')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'\{origin,prod,test\}', ret.stderr)

    def test_rerun(self):
        ret = self.deploy('rerun', 'test')
        cmd = r'ssh example.com cd /apps/02-test && deploy/after_push ' + \
            r'`git rev-parse HEAD@{1} HEAD` | tee -a log/deploy.log'

        assert [cmd] == self.get_executed_commands()
        assert ret.stderr == ''
        assert '> ' + cmd == self.replace_paths_in_output(ret.stdout).strip()
        assert ret.success
