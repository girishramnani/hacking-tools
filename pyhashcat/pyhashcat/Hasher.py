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

class SHA1Hasher(AbstractHasher):

    def getHash(self,data,asHex=False):
        sha1 = hashlib.sha1()
        sha1.update(data.encode())
        return sha1.hexdigest() if asHex else sha1.digest()

class SHA256Hasher(AbstractHasher):

    def getHash(self,data,asHex=False):
        sha256 = hashlib.sha256()
        sha256.update(data.encode())
        return sha256.hexdigest() if asHex else sha256.digest()
