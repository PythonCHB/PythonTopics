******************************
Where to put your custom code?
******************************

A suggestion for how to manage your personal library of python functions you might use for scripting, data analysis, etc.

TL; DR
======

If you have a collection of your own code you want access to for various projects:

Make a "package" out of it so you can manage it in one place, and use it in other places.

Introduction
------------

Many folks find they have a collection of little scripts and utilities that they want to be able to use and re-use for various projects. It is really NOT a good idea to simply copy and paste these around for use with each project -- you will regret that!

It is also not a good idea to use the ``PYTHONPATH`` environment variable to set up a directory in which to dump stuff. (Google a bit if you want to know why).

The best way to do this with Python is to use the python package mechanism.

A Python "package" is a collection of modules and scripts -- we usually think of these as something carefully developed for particular purpose and distributed to a wide audience for re-use -- the packages you can install with pip. Indeed that is the case, but the "collection of modules and scripts" part can be used for your own code that no one else is ever going to touch, and the overhead is small if you use it only this way.

Step by step:
-------------

1) Create a directory in your user (or home, or ... ) dir for your code. Let's call it "my_code".

2) This is going to seem odd, but create another dir with the same name inside that -- this is where the actual code goes. (it's a convention to name the top dir the same thing as the "package" name, but it doesn't matter. But the inner name does -- that is the name of your package.

3) In that dir, put in an empty, for now, file called ``__init__.py``.

4) In the outer dir, put in a file (we'll fill it in later) called ``setup.py``.

So you shoudl have::

  my_code
      my_code
          __init__.py
      setup.py

The inner my_code dir is now a python "package" -- any directory with a __init__.py file is a package. But how to use it?

The setup.py file is where you specify for python how this package is setup. You can do a lot in there, and if you ever want to share your code with anyone else, you should follow:

https://packaging.python.org/tutorials/distributing-packages/.

But for now, we are going to make it as *simple* as possible::

    from setuptools import setup

    setup(name='my_code',
          packages=['my_code'],
          )

That's it -- really! There is a lot you can do here to support multiple packages, scripts, etc, but this is enough to get you started.

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

To use this package, you need to "install" it into the python environment that you want to use. Some of us have a single python install -- maybe Anaconda's root environment, or the python.org python installer, or.... Some of us use virtualenv or conda environments. In any case, get yourself into that environment with a command line in the outer my_code dir, and type::

    python setup.py develop

"develop" is like install, but instead of copying the code into the python environment, it adds it to the python search path (only that particular python instances search path!) so you can import it, but it will always be importing the current version of the files if you change things.

Now you can fire up python (or ipython, or a Jupyter notebook, or write code in a script, or...) and do::

    from my_code import some_code

    In [2]: from my_code import some_code

    In [3]: some_code.test_fun()

    yup -- this worked!!

And you are good to go!

.. I've enclosed my sample package as a zip file -- if it makes it through.

NOTES:
------

If you have only a little bit of code, you can do all this with a single module, rather than a package, and have an easier import. But I think most folks have enough stuff that it's better to have multiple modules with related stuff in them.

If you have more than a few modules, it would probably make sense to keep them in separate packages, organized by functionality.

This is only the very simplest way to do it what you really SHOULD do is be more formal about the process:
  - Do some versioning of the package
  - Keep it in source code version control system (like git, etc)

and others...

Look up "Software Carpentry" for many more ideas how better to manage your software for Science.


