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

class AbstractKeyGenerator(metaclass=ABCMeta):
    """
    Use this class to implement you custom generator for more fine grain control over the
    keywords
    """

    def __init__(self,pattern=None):
        self.pattern = pattern

    def gen_keywords(self,length,*args,**kwargs):
        raise NotImplementedError


class NumericGenerator(AbstractKeyGenerator):

    def __init__(self,pattern):
        AbstractKeyGenerator.__init__(pattern)


