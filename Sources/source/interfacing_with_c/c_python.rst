########################
Interfacing C and Python
########################

Sorry, not much here yet.

NOTE: this is all about the CPython interpreter -- not PyPy, IronPython, JPython, etc.

Documentation:
==============

Core docs for the C API:


https://docs.python.org/3/extending/


Interfacing methods:
====================

There a bunch of ways to interface C and Python:


Hand write against the C API:
-----------------------------

The python interpeter exposes a full API to all the python objects, etc. You can essentially do anything, but it's a lot of hand-work.

And reference counting is really hard to get right!

http://docs.python.org/3/c-api/

Cython:
-------

Cython can be described as a "python-like language for writing python extensions"

It can be used essentially to speed up Python, but also to call Python from C.

https://cython.org/


ctypes
------

Ctypes comes with Python out of the box.


SWIG, SIP, ETC.
---------------

Auto wrapper generators.


EXAMPLE:
========

Same as the one for fortran: a automatic gain control filter:

:download:`agc_example/agc_c.c`

:download:`agc_example/agc_c_cy.pyx`

:download:`agc_example/agc_cython.pyx`

:download:`agc_example/agc_python.py` 




