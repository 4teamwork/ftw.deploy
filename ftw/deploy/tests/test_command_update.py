from pathlib import Path

from . import TestCase


class TestCommandSetup(TestCase):

    def test_update_fails_when_no_scripts_detected(self):
        ret = self.deploy('update')
        assert not ret.success
        assert ret.stdout == ''
        assert 'ERROR: Could not detect template.\n' == ret.stderr

    def test_update_works_when_scripts_detected(self):
        assert self.deploy('init', 'plone').success

        after_push = Path('deploy/after_push')
        after_push.write_bytes(b'')
        assert len(after_push.read_bytes()) == 0

        assert self.deploy('update').success
        assert len(after_push.read_bytes()) > 0

    def test_does_not_update_the_remotes_script(self):
        assert self.deploy('init', 'plone').success

        script = Path('scripts/setup-git-remotes')
        script.write_bytes(b'foo')
        assert b'foo' == script.read_bytes()

        assert self.deploy('update').success
        assert b'foo' == script.read_bytes()

    def test_non_existing_file_is_not_created(self):
        assert self.deploy('init', 'plone').success

        script = Path('deploy/pull')
        assert script.exists()

        script.unlink()
        assert not script.exists()

        assert self.deploy('update').success
        assert not script.exists()
