from abc import ABCMeta

__author__ = 'girish'



class AbstractKeyGenerator(metaclass=ABCMeta):


    def __init__(self,pattern=None):
        self.pattern = pattern

    def gen_keywords(self,length):
        raise NotImplementedError


class NumericGenerator(AbstractKeyGenerator):

    def __init__(self,pattern):
        AbstractKeyGenerator.__init__(pattern)


