import os
import stat
from pathlib import Path

from . import TestCase


class TestCommandInitPlone(TestCase):

    def test_creates_directories(self):
        assert not os.path.exists('deploy')
        assert not os.path.exists('tmp')
        assert not os.path.exists('scripts')

        ret = self.deploy('init', 'plone')
        assert ret.stderr == ''
        assert ret.success

        assert os.path.exists('deploy')
        assert os.path.exists('tmp')
        assert os.path.exists('scripts')

    def test_plone_template_scripts(self):
        filenames = ['deploy/after_push',
                     'deploy/pull',
                     'deploy/update_plone',
                     'scripts/setup-git-remotes']
        for name in filenames:
            assert not os.path.exists(name)

        ret = self.deploy('init', 'plone')
        assert ret.stderr == ''
        assert ret.success

        for name in filenames:
            assert os.path.exists(name)
            assert stat.S_IEXEC & os.stat(name).st_mode

    def test_log_exists(self):
        assert not os.path.lexists('log')
        assert self.deploy('init', 'plone').success
        assert os.path.lexists('log')

    def test_tmp_has_gitignore(self):
        assert not os.path.exists('tmp/.gitignore')
        assert self.deploy('init', 'plone').success
        assert os.path.lexists('tmp/.gitignore')
        assert Path('tmp/.gitignore').read_bytes() == b'*\n!.gitignore\n'
