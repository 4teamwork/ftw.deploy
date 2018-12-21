import os
import shlex
import subprocess
from pathlib import Path

from ..utils import copy_from_template


TEMPLATES = {}


class TemplateBase(object):
    name = None

    @staticmethod
    def register(klass):
        TEMPLATES[klass.name] = klass()

    def is_applied_to_project(self):
        return False

    def install(self):
        self.create_directories()
        self.install_scripts(update=False)
        self.link_log()
        self.tmp_gitignore()

    def update(self):
        self.install_scripts(update=True)

    def create_directories(self):
        Path('deploy').mkdir(exist_ok=True)
        Path('tmp').mkdir(exist_ok=True)
        Path('scripts').mkdir(exist_ok=True)

    def install_scripts(self, update):
        pass

    def link_log(self):
        if not os.path.lexists('log'):
            subprocess.check_call(shlex.split('ln -s var/log'))

    def tmp_gitignore(self):
        Path('tmp/.gitignore').write_bytes(b'*\n!.gitignore\n')

    def install_script(self, relpath, create=True, overwrite=True):
        if Path(relpath).exists() and not overwrite:
            return

        if not Path(relpath).exists() and not create:
            return

        copy_from_template(self.template(relpath), relpath)

    def template(self, relpath):
        return Path(__file__).parent.joinpath(self.name, relpath)
