from unittest.case import TestCase

__author__ = 'girish'

from pyhashcat.keyGenerator import AbstractKeyGenerator

from keyGenerator import stringSource,NumericGenerator, allSymbolGenerator


class GeneratorTestCase(TestCase):


    def test_only_numerical_generator(self):
        self.assertEqual(next(NumericGenerator().gen_keywords()),('0',)*8)

    def test_all_symbol_generator(self):
        gen = allSymbolGenerator(4).gen_keywords()


        self.assertEqual(next(gen),('0',)*4)

        for i in range(10**4-1):
            next(gen)
        self.assertEqual(next(gen),('a',)*4)





class SourceTest(TestCase):

    def setUp(self):
        self.generator = stringSource()

    def test_length(self):
        gen = self.generator.get_word(5)
        self.assertEqual(len(next(gen)),5)

    def test_answer(self):
        gen = self.generator.get_word(5)
        self.assertEqual(next(gen),('a',)*5)
        self.assertEqual(next(gen),tuple(['a',]*4+['b']))


class regexGeneratorAndSourceTest(TestCase):

    def setUp(self):
        self.small_pattern = "???"
        self.medium_pattern = "h??l? w??l?"
        self.num_pattern ="1??"