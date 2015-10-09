
__author__ = 'girish'

"""
Key generator provides different patterns and options to reduce the keyword search space.
The ways to provide control over the keywords are:

:param pattern -> accepts a regex like language to match pattern.
        "?" -> matching a single character
       length -> to provide the length of the keyword
       min-length,max-length -> provide min-max length of he keyword (will work only if length and pattern are not given)
       has_num,has_characters, has_symbols -> flags which will be true by default , can be set to control the search domain.

Key generator can also take a file as input which will work as a dictionary.
"""

import string
import itertools
from abc import ABCMeta,abstractmethod


class source(metaclass=ABCMeta):

    @abstractmethod
    def get_domain(self):
        pass

    def get_word(self,length):
        possible_chars = self.get_domain()
        yield from itertools.product(possible_chars,repeat=length)



class stringSource(source):

    def get_domain(self):
        return string.ascii_letters


class numericSource(source):

    def get_domain(self):
        return string.digits


class AbstractKeyGenerator(metaclass=ABCMeta):
    """
    Use this class to implement you custom generator for more fine grain control over the
    keywords
    """

    def __init__(self,length=None):
        if length ==None:
            self.length = 8
        else:
            self.length = length

    @abstractmethod
    def gen_keywords(self):
        pass

    def _gen_keywords(self,generator,pattern=None,max_keys=1000000,*args,**kwargs):
        temp_max_key = max_keys
        max_keys = 10**self.length

        if temp_max_key < max_keys:
            max_keys = temp_max_key

        yield from generator.get_word(self.length)



class NumericGenerator(AbstractKeyGenerator):

    def gen_keywords(self):
        return super(NumericGenerator, self)._gen_keywords(numericSource())


class CharacterGenerator(AbstractKeyGenerator):

    def gen_keywords(self):
        return super(CharacterGenerator, self)._gen_keywords(stringSource())


class allSymbolGenerator(AbstractKeyGenerator):

    def gen_keywords(self):
        yield from NumericGenerator(self.length).gen_keywords()

        yield from CharacterGenerator(self.length).gen_keywords()







