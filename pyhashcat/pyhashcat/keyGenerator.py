from abc import ABCMeta

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

class source(metaclass=ABCMeta):
    pass


class stringSource(source):

    def get_word(self,length):
        possible_chars = string.ascii_letters
        word = []
        yield from itertools.product(possible_chars,repeat=length)



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

    def gen_keywords(self,pattern=None,*args,**kwargs):
        raise NotImplementedError


class NumericGenerator(AbstractKeyGenerator):

    def __init__(self,length):
        AbstractKeyGenerator.__init__(length)


class CharacterGenerator(AbstractKeyGenerator):

    def __init__(self,length):
        super(CharacterGenerator, self).__init__(length)



    def gen_keywords(self,generator,pattern=None,max_keys=100000,*args,**kwargs):

        for i in range(max_keys):
            yield generator.get_word(self.length)












