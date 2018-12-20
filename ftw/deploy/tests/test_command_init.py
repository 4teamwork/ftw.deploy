import re

from . import TestCase


class TestCommandInit(TestCase):

    def test_requires_template(self):
        ret = self.deploy('init')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'the following arguments are required: template', ret.stderr)

    def test_templates_are_proposed_in_usage(self):
        ret = self.deploy('init')
        assert not ret.success
        assert ret.stdout == ''
        assert re.search(r'\{plone\}', ret.stderr)
