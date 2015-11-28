Pure Python FNV hash implementation
===================================

.. image:: https://travis-ci.org/znerol/py-fnvhash.svg?branch=master
    :target: https://travis-ci.org/znerol/py-fnvhash


Pure Python implementation of the FNV_ hash family with 100% test coverage.
Take a look at pyhash_ for use cases where performance is more important than
portability.

.. _FNV: http://isthe.com/chongo/tech/comp/fnv/
.. _pyhash: https://pypi.python.org/pypi/pyhash


Usage
-----

::
    >>> from fnvhash import fnv1a_32
    >>> hex(fnv1a_32(b'foo'))
    '0xa9f37ed7'


License
-------

The software is subject to the MIT license.
