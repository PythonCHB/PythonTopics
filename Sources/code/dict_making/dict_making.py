"""
an exploration of how the dict constructor knows whether it is
working with a MApping of a general iterable.  It looks like
the code is something like this:

if isinstance(input, collections.abc.Mapping):
    self.update = {key: input[key] key in input}
else:
    self.update = {key: val for key, val in input}

So if your custom class present themapping interface -- that is, iterating
over it returns the keys, than you want to be a MApping ABC subclass.ABC

But if your custom class is not a Mapping, then you want __iter__ to return an
iterator over teh key, value pairs.
"""

from collections.abc import Mapping


def test_iter(instance):
    yield ("this")
    yield ("that")


class DictTest(Mapping):

    def __init__(self, this="this", that="that"):
        self.this = this
        self.that = that

    def __iter__(self):
        print("iter called")
        return test_iter(self)

    def __getitem__(self, key):
        return getattr(self, key)

    def __len__(self):
        print("__len__ called")


if __name__ == "__main__":

    dt = DictTest()
    print(dict(dt))

    dt = DictTest(this=45, that=654)
    print(dict(dt))


