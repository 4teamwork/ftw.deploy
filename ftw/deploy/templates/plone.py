from pathlib import Path

from .base import TemplateBase


@TemplateBase.register
class PloneTemplate(TemplateBase):
    name = 'plone'

    def is_applied_to_project(self):
        return Path('deploy/update_plone').exists()

    def install_scripts(self, update):
        self.install_script('deploy/after_push', create=not update)
        self.install_script('deploy/pull', create=not update)
        self.install_script('deploy/update_plone', create=not update)
        self.install_script('scripts/setup-git-remotes', overwrite=False)
