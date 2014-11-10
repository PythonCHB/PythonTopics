
.. Weak References slides file, created by
   hieroglyph-quickstart on Mon Mar 10 21:33:01 2014.


*********************************************
Python Memory Management and Weak References
*********************************************

Chris Barker

``PythonCHB@gmail.com``

``https://github.com/PythonCHB``

==================
Memory Management
==================

..  rst-class:: left

 * You don't want python objects that are no longer in use taking up memory.
 * You don't want to keep track of all that yourself.
 * Most "scripting languages" or "virtual machines" have some sort of
   automated memory management

.. rst-class:: center medium

    Many ways to do "Garbage Collection"


Reference Counting
--------------------

How memory is managed is not part of the Python language spec:
 * Jython uses the JVM
 * Iron Python uses the CLR
   - Both are garbage collected
 * PyPy uses Minimark_

 .. _Minimark:  https://pypy.readthedocs.org/en/release-2.4.x/garbage_collection.html#minimark-gc


The CPython interpreter uses a reference counting scheme:
 * Every time there is a new reference to a Python object, its reference
   count is increased
 * Every time a reference is removed -- the count is decreased
 * When the reference count goes to zero: the object is deleted
   (memory freed)


What makes a reference?
------------------------

* Binding to a name::

   x = an_object

* Putting it in a container::

   l.append(an_object)

* Passing it to a function::

   func(an_object)

Most of the time, you don't need to think about this at all.


How do I see what's going on?
------------------------------

.. code-block:: python


  import sys
  sys.getrefcount(object)


**NOTE:** This will always return one more than you'd expect, as passing the object to the function increases its refcount by one:

.. code-block:: ipython

  In [5]: a = []

  In [6]: sys.getrefcount(a)
  Out[6]: 2

The Heisenberg Uncertainty Principle:
   - you can't observe it without altering it


Playing with References
------------------------

(live demo)

.. code-block:: ipython

	In [7]: a = []

	In [8]: sys.getrefcount(a)
	Out[8]: 2

	In [9]: b = a

	In [10]: sys.getrefcount(a)
	Out[10]: 3

	In [11]: l = [1,2,3,a]

	In [12]: sys.getrefcount(a)
	Out[12]: 4

.. nextslide::

.. code-block:: ipython

	In [13]: del b

	In [14]: sys.getrefcount(a)
	Out[14]: 3


	In [15]: del l

	In [16]: sys.getrefcount(a)
	Out[16]: 2


.. nextslide::


.. code-block:: ipython

    # function local variables

	In [17]: def test(x):
	   ....:     print "x has a refcount of:", sys.getrefcount(x)
	   ....:

	In [18]: sys.getrefcount(a)
	Out[18]: 2

	In [19]: test(a)
	x has a refcount of: 4

	In [20]: sys.getrefcount(a)
	Out[20]: 2


.. nextslide::

.. code-block:: ipython

	In [21]: x = 3

	In [22]: sys.getrefcount(x)
	Out[22]: 428

WHOA!!

(hint: interning....)


The Power of Reference Counting
--------------------------------


* You don't need to think about it most of the time.

* Code that creates objects doesn't need to delete them

* Objects get deleted right away

   . They get "cleaned up" (files, for instance)

* Performance is predictable


The Limits of Reference Counting
--------------------------------

* Performance overhead on all operations. But the big one:

.. rst-class:: medium

  Circular references

If a python object references another object that references the first
object: You have a circular reference:

....

.. nextslide::

.. code-block:: ipython

    In [8]: l1 = [1,] ; l2 = [2,]

    In [9]: l1.append(l2); l2.append(l1)

    In [10]: l1
    Out[10]: [1, [2, [...]]]

    In [11]: l2
    Out[11]: [2, [1, [...]]]

    In [12]: l1[1]
    Out[12]: [2, [1, [...]]]

    In [13]: l2[1][1][1]
    Out[13]: [1, [2, [...]]]

    In [16]: sys.getrefcount(l1)
    Out[16]: 12


The Garbage Collector
-----------------------

As of Python 2.0 -- a garbage collector was added.

It can find and clean up "unreachable" references.

It is turned on by default::

	In [1]: import gc

	In [2]: gc.isenabled()
	Out[2]: True

or you can force it::

	In [4]: gc.collect()
	Out[4]: 64

But it can be slow, and doesn't always work!

Examples
----------


Example in iPython notebook::

  code/CircularReferenceExample.ipynb

You can also run::

  circular.py

And::

  memcount.py

``mem_check.py`` is code that reports process memory use
  -- only *nix for now -- sorry!

Weak References
-----------------

For times when you don't want to keep objects alive, Python provides
"weak references".

You saw this in the examples.

Three ways to use them:

* The built-in containers:
  - ``WeakKeyDictionary``
  - ``WeakValueDictionary``
  - ``WeakSet``

* ``Proxy`` objects
  - act much like regular references -- client code doesn't know the difference
* ``WeakRef`` objects
  - When you want to control what happens when the referenced object is gone.

Exercise
---------

Build a "weak cache":

For large objects that are expensive to create:

* Use a WeakValueDictionay to hold references to (probably large) objects.

* When the client requests an object that doesn't exist -- one is created, returned, and cached (weakly).

* If the object is in the cache, it is returned.

* when not other references exist to the object, it is NOT retained by the cache.

