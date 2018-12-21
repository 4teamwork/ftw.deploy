import shutil
from pathlib import Path

from . import VERSION


def copy_from_template(template, target, executable=True):
    template = Path(template)
    target = Path(target)

    shutil.copy(template, target)

    content = target.read_bytes()
    content = content.replace(b'{{ftw.deploy version}}',
                              f'ftw.deploy {VERSION}'.encode('utf-8'))
    target.write_bytes(content)
