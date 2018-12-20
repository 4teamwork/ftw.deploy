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


**Initialize deploy scripts**

The first step in a fresh project is to initialize the deployment scripts.
This can be done with ``deploy init plone``.
This will create scripts in the folders ``deploy`` and ``scripts``.

**Installing deployment and configuring the remote**

Next, install the deployment on the server by cloning the repository and
performing installation steps.
Then adapt ``scripts/setup-git-remotes`` with the deployment location and execute it.

**Setup hook**

For installing the ``post-receive`` hook and configuring the repository execute the
``deploy setup [remote]`` command.

**Update scripts**

You can update existing scripts in a project with ``deploy update``.

**Installing an update**

When all is set up, you can simply push on the ``master``-branch  of the remote in
order to install an update. Examples:

.. code::

   git push prod master
   git push test my-branch:master
   git push prod test/master:master

**Rerun a deployment**

If you need to rerun a deployment, simply use ``deploy rerun [remote]``.


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
