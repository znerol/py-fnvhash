"""
FNV hash test suite.

Derived from http://isthe.com/chongo/src/fnv/test_fnv.c
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import fnvhash
from fnvhash.test import vector
from unittest import TestCase

class FNVTest(TestCase):
    """
    FNV hash test suite.
    """

    def test_fnv0_32(self):
        """
        Tests the 32 bit FNV-0 hash implementation.
        """
        for string, expected_hval in vector.fnv0_32_vector.items():
            result = fnvhash.fnv0_32(string)
            self.assertEqual(result, expected_hval)

    def test_fnv1_32(self):
        """
        Tests the 32 bit FNV-1 hash implementation.
        """
        for string, expected_hval in vector.fnv1_32_vector.items():
            result = fnvhash.fnv1_32(string)
            self.assertEqual(result, expected_hval)

    def test_fnv1a_32(self):
        """
        Tests the 32 bit FNV-1a hash implementation.
        """
        for string, expected_hval in vector.fnv1a_32_vector.items():
            result = fnvhash.fnv1a_32(string)
            self.assertEqual(result, expected_hval)

    def test_fnv0_64(self):
        """
        Tests the 64 bit FNV-0 hash implementation.
        """
        for string, expected_hval in vector.fnv0_64_vector.items():
            result = fnvhash.fnv0_64(string)
            self.assertEqual(result, expected_hval)

    def test_fnv1_64(self):
        """
        Tests the 64 bit FNV-1 hash implementation.
        """
        for string, expected_hval in vector.fnv1_64_vector.items():
            result = fnvhash.fnv1_64(string)
            self.assertEqual(result, expected_hval)

    def test_fnv1a_64(self):
        """
        Tests the 64 bit FNV-1a hash implementation.
        """
        for string, expected_hval in vector.fnv1a_64_vector.items():
            result = fnvhash.fnv1a_64(string)
            self.assertEqual(result, expected_hval)
