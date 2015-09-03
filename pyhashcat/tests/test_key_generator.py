from unittest.case import TestCase

__author__ = 'girish'

from pyhashcat.keyGenerator import AbstractKeyGenerator

class NumericalGeneratorTestCase(TestCase):


    def setUp(self):
        self.small_pattern = "???"
        self.medium_pattern = "h??l? w??l?"
        self.num_pattern ="1??"

    def test_only_numerical_generator(self):
        pass

