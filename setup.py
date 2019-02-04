import os

from setuptools import find_packages
from setuptools import setup


version = '1.2.1.dev0'


setup(name='ftw.deploy',
      version=version,
      description='Tooling and scripts for git push based deployment at 4teamwork.',

      long_description=(
          open('README.rst').read() + '\n'
          + open(os.path.join('docs', 'HISTORY.txt')).read()),

      classifiers=[
          'Intended Audience :: Developers',
      ],

      keywords='ftw deploy',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.deploy',

      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw', ],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
      ],
      tests_require=[
      ],

      entry_points={
          'console_scripts': ['deploy = ftw.deploy.command:main']
      })
