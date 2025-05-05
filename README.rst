Pure Python FNV hash implementation
===================================

|Build Status| |Package Version|


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

.. |Build Status| image:: https://github.com/znerol/py-fnvhash/actions/workflows/on-push.yml/badge.svg
   :target: https://github.com/znerol/py-fnvhash/actions/workflows/on-push.yml
.. |Package Version| image:: https://img.shields.io/pypi/v/fnvhash.svg
   :target: https://pypi.python.org/pypi/fnvhash
