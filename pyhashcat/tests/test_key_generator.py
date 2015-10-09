from unittest.case import TestCase

__author__ = 'girish'

from pyhashcat.keyGenerator import AbstractKeyGenerator

from keyGenerator import stringSource


class NumericalGeneratorTestCase(TestCase):


    def setUp(self):
        self.small_pattern = "???"
        self.medium_pattern = "h??l? w??l?"
        self.num_pattern ="1??"

    def test_only_numerical_generator(self):
        pass



class stringSourceTest(TestCase):

    def setUp(self):
        self.generator = stringSource()

    def test_length(self):
        gen = self.generator.get_word(5)
        self.assertEqual(len(next(gen)),5)

    def test_answer(self):
        gen = self.generator.get_word(5)
        self.assertEqual(next(gen),('a',)*5)
        self.assertEqual(next(gen),tuple(['a',]*4+['b']))

