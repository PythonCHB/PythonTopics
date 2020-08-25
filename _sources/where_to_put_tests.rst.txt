*******************
Where to Put Tests?
*******************

======
TL; DR
======


If your package and test code are small and self contained, put the tests in with the package.

If the tests are large or complex, or require reading/writing files, or significant sample data, put your tests outside the package.

Test system recommendations
----------------------------

``pytest`` has a bit of discussion of the issue here:

https://docs.pytest.org/en/stable/goodpractices.html

For ``nose``, read https://nose.readthedocs.io/en/latest/finding_tests.html

and for ``unittest`` read https://docs.python.org/3/library/unittest.html#test-discovery .


Two Options
-----------

In Python packaging, there is no consensus on where you should put your test suite. This thread:

https://mail.python.org/pipermail/distutils-sig/2015-October/027003.html

makes that clear :-)

There are essentially two recommended approaches:

1) Put all your test code outside the package, and have it all designed to import from an installed base::

    from my_package import the_module_to_test

to do that, you need to install your package under development in "develop" mode::

    python setup.py develop

or::

    pip install -e .   # install package using setup.py in editable mode

That means that you do need a setup.py -- though it can be very minimal. See:

https://packaging.python.org/en/latest/

for recommendations.

In the this case, the directory with all the tests should not be a python package -- this is, it should not have a ``__init__.py`` file.


2) The other options is to put your test code in a sub-package inside your package. In this case, it should be inside your package, and *be* a python package itself (i.e. have an ``__init__.py``)::

    my_package
        __init__.py
        module_1.py
        module_2.py
        test
            __init_.py
            test_1.py
            test_2.py

Self Contained
--------------

The advantage of keeping test code self-contained is that you can have a large suite of tests with sample data and who knows what, and it won't bloat and complicate the installed package (and test code can write to the test dirs, etc. Also, you can then run the test suite against an installed version that may not be exactly the same as the current live code.

Sub-package
-----------

The advantage of test being a sub-package is that your test code gets installed with the package, so users (including yourself, if you are deploying the code) can install the package, and run the test to make sure the install all went well. You can also have the tests use relative imports, so you can run it all without installing (though with develop mode I don't think that is much of an advantage)


