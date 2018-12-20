import re

from . import TestCase


class TestCommandSetup(TestCase):

    def test_requires_remote_name(self):
        ret = self.deploy('setup')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'the following arguments are required: remote', ret.stderr)

    def test_existing_remotes_are_proposed_in_usage(self):
        ret = self.deploy('setup')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'\{origin,prod,test\}', ret.stderr)

    def test_setup_stubbed_commands(self):
        ret = self.deploy('setup', 'test')
        assert [
            'scp {ftw.deploy/scripts}/post-receive example.com:/apps/02-test/.git/hooks/post-receive',
            'ssh example.com cd /apps/02-test && git config --bool receive.denyNonFastForwards false',
            'ssh example.com cd /apps/02-test && git config receive.denyCurrentBranch ignore',
        ] == self.get_executed_commands()

        assert ret.stderr == ''
        assert [
            '> scp {ftw.deploy/scripts}/post-receive example.com:/apps/02-test/.git/hooks/post-receive',
            '> ssh example.com cd /apps/02-test && git config --bool receive.denyNonFastForwards false',
            '> ssh example.com cd /apps/02-test && git config receive.denyCurrentBranch ignore',
        ] == self.replace_paths_in_output(ret.stdout).splitlines()
        assert ret.success
