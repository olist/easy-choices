How to contribute
==================

We welcome contributions of many forms, for example:

- Code (by submitting pull requests)
- Documentation improvements
- Bug reports and feature requests

General guideline
-----------------

easy-choices is a library built to be used by community in several projects, for that reason, try do not:

* Include compiled dependencies (binaries or platform-specific)
* Include code without tests and documentation
* Include application specific code (eg, it could be reused?)
* Dependency pin
* Do not break backward compatibility


Local installation
------------------

First of all, it's assumed that you have virtualenv installed on your machine.

Clone our repository:

.. code-block:: shell

   $ git clone git@github.com:olist/easy-choices.git

   $ cd easy-choices

Create a virtualenv:

.. code-block:: shell

   $ virtualenv .venv

Activate it:

.. code-block:: shell

   $ source .venv/bin/activate

Then install the requirements of development:

.. code-block:: shell

   $ make dev-requirements


Tests
-----

We use ``pytest`` and to avoid a flood of fixtures, try to isolate your tests
and your fixtures inside a folder within ``tests`` folder.

Common fixutres are allowed, but think if they make sense to any other code
reuse that fixture.

Before running our test suite it's assumed that you have already installed the requirements of development.

Run tests executing the following command:

.. code-block:: shell

   $ make test
