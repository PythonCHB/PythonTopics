******************************
Where to put your custom code?
******************************


A Package Just for You!
=======================

(You can find this page at: http://bit.ly/JustPackage)

.. note:: This page is generated from a Sphinx document managed in this gitHub repo: https://github.com/PythonCHB/PythonTopics. I welcome questions, comments, and, of course, Pull Requests.


A suggestion for how to manage your personal library of python functions you might use for scripting, data analysis, etc.


TL; DR
======

If you have a collection of your own code you want to access for various projects:

Make a "package" out of it so you can manage it in one place, and use it in other places.

You DO NOT NEED TO PUT IT ON PYPI !


Introduction
------------

Many scientists and engineers that do a little coding find they have a collection of little scripts and utilities that they want to be able to use and re-use for various projects.

Options for Handling Your Code Collection:
------------------------------------------

**(1)** Keep your code in one place and copy and paste the functions you need into each new project.

.. centered:: **DON'T DO THAT!**

.. centered:: **REALLY!**


It is really NOT a good idea to simply copy and paste code around for use with each project. You will end up with multiple versions scattered all over the place ...

.. centered:: **You will regret that!**


**(2)** Put your code in a single directory and add it to the ``PYTHONPATH`` environment variable

.. centered:: **DON'T DO THAT!**

.. centered:: **REALLY!**


``PYTHONPATH`` is shared by all installs of Python. What with Python2, Python3, virtual environments, etc -- it's really not a good idea.

If you don't believe me: **Google It**


What you should do is make a "package"
--------------------------------------

The best way to do this with Python is to use the Python package mechanism.

A Python "package" is a collection of modules and scripts -- we usually think of these as something carefully developed for a particular purpose and distributed to a wide audience for re-use -- the packages you can install with pip.

Indeed that is the case, but the "collection of modules and scripts" part can be used for your own code that no one else is ever going to touch, and the overhead is small if you use it only this way.


Why Don't People Tend to Figure This out for Themselves?
........................................................

The packaging documentation is mostly about making a "proper" package for distribution to a wide audience.

So newbies tend to either:

* Think: "I don't want/need to do all that", and then move on and copy and past their code around like they have already been doing.

or

* Go ahead and follow all the instructions, and end up putting their tiny little not-useful-to-anyone-else package up on PyPi.


The challenge is that most of the documentation about python packaging is focused on creating a package of a library that you want to distribute to the community. In that case, it's very important to have full and proper meta data, tests, documentation, etc. As a result, the packaging documentation makes the whole process seem complicated and cumbersome.

.. rubric:: Making a simple package just for your own use can be very simple, and very useful.


Step by Step:
-------------

1) Create a directory in your user (or home, or ... ) dir for your code. Let's call it "my_code".

2) This is going to seem odd, but create another dir with the same name inside that -- this is where the actual code goes. (it's a convention to name the top directory the same thing as the "package" name, but you don't have to follow that convention. But the inner name does matter -- that is the name of your package, and how you will import it into Python.

Be thoughtful about what you name your package: you want a easy to remember and fairly easy to type name, but also one that is not used already for any of the standard library or commonly used third party packages. Once you come up with a name, google "the_name python" just to make sure it's not already in use.

3) In that dir, put in an empty, for now, file called ``__init__.py``.

4) In the outer dir, put in a file (we'll fill it in later) called ``setup.py``.

So you should have::

  my_code
      my_code
          __init__.py
          some_code.py
      setup.py

The inner my_code dir is now a python "package" -- any directory with a ``__init__.py`` file is a package. But how to use it?

The ``setup.py`` file is where you specify for python how this package is setup. You can do a lot in there, and if you ever want to share your code with anyone else, you should follow:

https://packaging.python.org/tutorials/distributing-packages/

But for now, we are going to make it as *simple* as possible::

    from setuptools import setup

    setup(name='my_code',
          packages=['my_code'],
          )

That's it -- really! There is a lot you can do here to support multiple packages, scripts, etc, but this is enough to get you started.

Here: :download:`make_my_package.py <../code/make_my_package.py>` is a little script that will build an empty package for you::

  python make_my_package.py your_package_name

will do it for you.

Putting in your code
--------------------

Now put some code in there!

Create a file for your code, and put it in the inner my_code dir:

``some_code.py``::

    #!/usr/bin/env python

    """
    Just an example, but this could be a collection of utility functions, etc.

    Here would be documentation of what's in this file

    In this case, just one function to make sure it works.
    """

    def test_fun():
        print("yup -- this worked!!")

OK -- now you have a (useless) package with some code in it - how to use it?

To use this package, you need to "install" it into the python environment that you want to use. Some of us have a single python install -- maybe Anaconda's root environment, or the python.org python installer, or ...

Some of us use virtualenv, or pipenv, or conda environments. In any case, get yourself into that environment at a command line and put yourself (``cd`` in Terminal, DOS box, etc...)  in the outer my_code dir (where the setup.py  is), and type::

    pip install -e .

``pip install`` installs a package. ``-e`` means "do an editable install", and the dot (``.``) tells pip to install the package in the current directory. ``pip`` will look for a ``setup.py`` file in the current working dir. An editable install is like install, but instead of copying the code into the python environment, it adds it to the Python search path (only that particular environment's Python) so you can import it, but it will always be importing the current version of the files if you change things.

This means you can be actively maintaining your shared code, and other projects that use it will always get the latest version.

Now you can fire up Python (or iPython, or a Jupyter notebook, or write code in a script, or...) and do:

.. code-block:: ipython

    In [2]: from test_package import test_code

    In [3]: test_code.test_fun()

    yup -- this worked!!

And you are good to go!

.. Here is a zip file of my simple example package: :download:`my_code.zip <../code/my_code.zip>`


NOTES:
------

If you have only a little bit of code, you can do all this with a single module, rather than a package, and have an easier import. But I think most folks have enough stuff that it's better to have multiple modules with related stuff in them.

If you have more than a few modules, it would probably make sense to keep them in separate packages, organized by functionality.

This is only the very simplest way to do it. What you really SHOULD do is be more formal about the process:
  - Do some versioning of the package
  - Keep it in source code version control system (like git, etc)
  - Add tests of your code...

and others. But this is enough to get you started, and you can extend it as you develop more software carpentry skills.

Look up "Software Carpentry" for many more ideas about how better to manage your Software for Science.


