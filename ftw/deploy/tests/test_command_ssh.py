import re

from . import TestCase


class TestCommandSSH(TestCase):

    def test_requires_remote_name(self):
        ret = self.deploy('ssh')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'the following arguments are required: remote', ret.stderr)

    def test_existing_remotes_are_proposed_in_usage(self):
        ret = self.deploy('ssh')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'\{origin,prod,test\}', ret.stderr)

    def test_ssh_without_options(self):
        ret = self.deploy('ssh', 'test')
        cmd = r'ssh example.com -t cd /apps/02-test; bash --login'

        assert [cmd] == self.get_executed_commands()
        assert ret.stderr == ''
        assert ('connecting to:       example.com\n'
                'change directory to: /apps/02-test\n'
                '\n'
                '> ssh example.com -t cd /apps/02-test; bash --login'
                ) == self.replace_paths_in_output(ret.stdout).strip()
        assert ret.success

    def test_ssh_with_custom_user(self):
        ret = self.deploy('ssh', '--user', 'zope', 'test')
        assert ret.stderr == ''
        cmd = r'ssh zope@example.com -t cd /apps/02-test; bash --login'
        assert [cmd] == self.get_executed_commands()

    def test_ssh_with_overwriting_custom_user(self):
        ret = self.deploy('ssh', 'prod')
        assert ret.stderr == ''
        cmd = r'ssh zope@example.com -t cd /apps/01-prod; bash --login'
        assert [cmd] == self.get_executed_commands()

        self.purge_executed_commands()

        ret = self.deploy('ssh', '--user', 'me', 'prod')
        assert ret.stderr == ''
        cmd = r'ssh me@example.com -t cd /apps/01-prod; bash --login'
        assert [cmd] == self.get_executed_commands()

    def test_ssh_with_ssh_parameters(self):
        ret = self.deploy('ssh', 'test', '-L 10101:localhost:10101')
        assert ret.stderr == ''
        cmd = r'ssh -L 10101:localhost:10101 example.com -t cd /apps/02-test; bash --login'
        assert [cmd] == self.get_executed_commands()

    def test_ssh_with_tunnel_option(self):
        ret = self.deploy('ssh', '--tunnel', 'test')
        assert ret.stderr == ''

        ports_to_tunnel = (
            10200,  # instance0
            10201,  # instance1
            10202,  # instance2
            10203,  # instance3
            10204,  # instance4
            10210,  # instancepub
            10230,  # solr
            10250,  # haproxy
        )

        cmd = r'ssh {} example.com -t cd /apps/02-test; bash --login'.format(
            ' '.join(['-L {0}:localhost:{0}'.format(port) for port in ports_to_tunnel])
        )
        self.maxDiff = None
        assert [cmd] == self.get_executed_commands()

    def test_ssh_with_tunnel_option_failes_wihtout_deployment_number(self):
        ret = self.deploy('ssh', '--tunnel', 'origin')
        assert not ret.success
        assert ret.stdout == ''
        assert 'ERROR: Could not find deployment number of remote.\n' == ret.stderr
