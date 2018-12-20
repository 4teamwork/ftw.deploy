ftw.deploy
==========

``ftw.deploy`` provides opinionated tooling for git-push based deployment setups.
The tool helps installing hooks and deployment scripts.


Installation
------------

``ftw.deploy`` simply provides a ``deploy`` command as console script.
It requires Python 3!

The package can be installed with ``pip`` in combination with your favorite
way of isolation / virtual-env.
You may want to use `pipsi <https://github.com/mitsuhiko/pipsi>`_ for installation.


Usage
-----

After installation, should have a ``deploy`` command available.
The most recent documentation is available with ``deploy help``.


Development
-----------

In order to develop ``ftw.deploy``, you need to install
`pipenv <https://pipenv.readthedocs.io>`_ and follow these instructions:

.. code::

  $ git clone git@github.com:4teamwork/ftw.deploy.git
  $ cd ftw.deploy
  $ pipenv install
  $ pipenv shell
  $ deploy --help


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.deploy`` is licensed under GNU General Public License, version 2.
