import re

from . import TestCase


class TestCommandHelp(TestCase):

    def test(self):
        ret = self.deploy('help')
        assert ret.success
        assert re.match(r'^usage: ', ret.stdout)
        assert ret.stderr == ''
