__author__ = 'girish'


from abc import ABCMeta, abstractmethod


class AbstractHasher(metaclass=ABCMeta):


    @abstractmethod
    def getHash(self,data):
        raise NotImplementedError




class Hasher(AbstractHasher):

    def __init__(self):
        pass
