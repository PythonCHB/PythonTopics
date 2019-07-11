#!/usr/bin/env python

"""
A simple script that builds a as_simple_as_possible package
to use for your own code.
"""
import sys, os

USAGE = """
python make_my_package.py your_package_name

Running the script will create a minimal package
you can use to manage your personal code
"""

setup_template = """#!/usr/bin/env python
from setuptools import setup

setup(name='{package_name}',
      packages=['{package_name}'],
      )

"""

test_code = '''#!/usr/bin/env python

"""
Just an example, but this could be a collection of utility functions, etc.

Here would be documentation of what's in this file

In this case, just one function to make sure it works.
"""

def test_fun():
    print("yup -- this worked!!")

'''

if __name__ == "__main__":


    try:
        package_name = sys.argv[1]
    except IndexError:
        print("You need to provide a name for your package")
        print(USAGE)
        sys.exit(1)

    this_dir = os.curdir
    os.mkdir(package_name)
    os.chdir(package_name)
    with open("setup.py", 'w') as setupfile:
        setupfile.write(setup_template.format(package_name=package_name))
    os.mkdir(package_name)
    os.chdir(package_name)
    with open("__init__.py", 'w') as initfile:
        initfile.write("#!/usr/bin/env python\n\n"
                       "__version__ = '0.0.0'\n"
                       )

    with open("test_code.py", 'w') as initfile:
        initfile.write(test_code)

    os.chdir("../..")





