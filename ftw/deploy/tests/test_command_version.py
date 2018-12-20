import re

from . import TestCase


class TestCommandVersion(TestCase):

    def test(self):
        ret = self.deploy('--version')
        assert ret.success
        assert re.match(r'^(\d\.){3}dev0$', ret.stdout.strip())
        assert ret.stderr == ''
