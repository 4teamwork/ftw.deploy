ftw.deploy
==========

``ftw.deploy`` provides opinionated tooling for git-push based deployment setups.
The tool helps installing hooks and deployment scripts.

.. contents:: Table of Contents


Installation
------------

``ftw.deploy`` simply provides a ``deploy`` command as console script.
It requires Python 3!

The package can be installed with ``pip`` in combination with your favorite
way of isolation / virtual-env.

Example:

.. code::

   $ python3 -m venv ftw.deploy
   $ cd ftw.deploy
   $ source bin/activate
   $ ./bin/pip install ftw.deploy

   # sym-link the deploy script into your PATH
   $ ln -s `pwd`/bin/deploy ~/bin
   $ deploy --help


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

**Connect to the deployment with ssh**

``ftw.deploy`` provides a shortcut for connecting with ssh and cd'ing into
the deployment directory ``deploy ssh [remote]``.


Templates
---------

Plone
~~~~~

The plone template contains push deployment scripts which are optimized for use in
combination with `ftw.buildouts <https://github.com/4teamwork/ftw-buildouts>`_.


Custom update script
++++++++++++++++++++

The ``deploy/after_push`` script can be configured to run another script
than ``deploy/update_plone``.

For example you could add a ``scripts/nightly-reinstall`` and then add to
your nightly buildout configuration file:

.. code::

    [buildout]
    deployment-update-plone-script = scripts/nightly-reinstall

Be aware that this must be in the ``buildout.cfg`` of the deployment (which
may be a symlink), but it can not be extended since the buildout config file
is not parsed recursively for this option.


Advanced Usage
--------------

VPN without SSH
~~~~~~~~~~~~~~~

When the deployment is in a VPN without SSH access, we cannot push to the
deployment.
In this situation the ``deploy/pull`` script can be used for simulating a push.
It pulls from the upstream (the branch must have an upstream defined) and runs
the deployment scripts.


Zero Downtime
~~~~~~~~~~~~~

When upgrades need to be installed, the script normally takes the site offline
in order to prevent conflicting writes to the database while the upgrades run.

When having a zero downtime environment, such as when only a publihser writes
the database (which is stopped while running upgrades), it is safe to keep the
site running for anonymous users.

In order to enable this behavior you must set the ``deployment-zero-downtime``
option in the buildout configurations which should be upgraded in zero downtime
mode.

**WARNING:** The ``deployment-zero-downtime`` must be in the ``buildout.cfg`` file
of the deployment. It does not work when using ``extend`` for this option since
the option is directly read from ``buildout.cfg``.

Example:

.. code::

    [buildout]
    extends =
        ...

    deployment-zero-downtime = true

Deploy one commit with zero downtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When deploying a commit with upgrade steps, the site will be taken offline
unless zero downtime is configured.
But sometimes we want to deploy a commit with (fast) upgrades to a
non-zero-downtime deployment, but without downtime.
For marking a commit as "zero-downtime proof", you can push it to the branch
`zero-downtime` on the deployment remote, before doing a regular deployment.

.. code::

    $ git push testing master:zero-downtime
    $ git push testing master


Activate zero downtime by environment variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using deploy/pull, we can activate the zero downtime strategy
with an environment variable:

Example:

.. code::

   $ ZERO_DOWNTIME=true deploy/pull


Development
-----------

In order to develop ``ftw.deploy``, you need to install
`pipenv <https://pipenv.readthedocs.io>`_ and follow these instructions:

.. code::

  $ git clone git@github.com:4teamwork/ftw.deploy.git
  $ cd ftw.deploy
  $ pipenv install --dev
  $ pipenv shell
  $ deploy --help
  $ pytest


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.deploy`` is licensed under GNU General Public License, version 2.
