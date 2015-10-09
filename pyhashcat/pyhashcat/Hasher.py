__author__ = 'girish'


from abc import ABCMeta, abstractmethod
import hashlib

class AbstractHasher(metaclass=ABCMeta):


    @abstractmethod
    def getHash(self,data,asHex=False):
        raise NotImplementedError



class MD5Hasher(AbstractHasher):

    def getHash(self,data,asHex=False):
        md5 = hashlib.md5()
        md5.update(data.encode())
        return md5.hexdigest() if asHex else md5.digest()
