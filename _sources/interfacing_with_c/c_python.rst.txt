Interfacing C and Python
################################

Sorry, not much here

NOTE: this is all about the CPython interpreter -- not PyPy, IronPython, JPython, etc.

Documentation:
================

Core docs for the C API:




Interfacing methods:
======================

There a bunch of ways to interface C and Python:

Hand write against the C API:
------------------------------

The python interpeter exposes a full API to all teh pyton objects, etc. You can essentially do anything, but it's a lot of hand-work.

And reference counting is really hard to get right!

http://docs.python.org/2/c-api/

Cython:
------------------

Cython can be described as a "python-like language for writing python extensions"

It can be used essentially to speed up Python, but also to Call Python from C

(derived from Pyrex)

XDress
........

ctypes
--------


SWIG, SIP, ETC.
----------------

Auto wrapper generators.


EXAMPLE:
============

Same as the one for fortran: a automatic gain control filter.