import os
import shlex
import shutil
import stat
import subprocess
from pathlib import Path


TEMPLATES = {}


class TemplateBase(object):
    name = None

    @staticmethod
    def register(klass):
        TEMPLATES[klass.name] = klass

    def install(self):
        self.create_directories()
        self.install_scripts()
        self.link_log()
        self.tmp_gitignore()

    def create_directories(self):
        Path('deploy').mkdir(exist_ok=True)
        Path('tmp').mkdir(exist_ok=True)
        Path('scripts').mkdir(exist_ok=True)

    def install_scripts(self):
        pass

    def link_log(self):
        if not os.path.lexists('log'):
            subprocess.check_call(shlex.split('ln -s var/log'))

    def tmp_gitignore(self):
        Path('tmp/.gitignore').write_bytes(b'*\n!.gitignore\n')

    def install_script(self, relpath):
        shutil.copyfile(self.template(relpath), Path(relpath))
        os.chmod(relpath, os.stat(relpath).st_mode | stat.S_IEXEC)

    def template(self, relpath):
        return Path(__file__).parent.joinpath(self.name, relpath)
