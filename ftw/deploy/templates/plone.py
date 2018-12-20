from .base import TemplateBase


@TemplateBase.register
class PloneTemplate(TemplateBase):
    name = 'plone'

    def install_scripts(self):
        self.install_script('deploy/after_push')
        self.install_script('deploy/pull')
        self.install_script('deploy/update_plone')
        self.install_script('scripts/setup-git-remotes')
