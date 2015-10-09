__author__ = 'girish'
from unittest import TestCase
import unittest

from pyhashcat.Hasher import MD5Hasher


from pyhashcat.Hasher import AbstractHasher


class hasher_test(TestCase):


    def setUp(self):
        self.data = "Nobody inspects the spammish repetition"
        self.hasher = MD5Hasher()

    def test_if_abstract_hasher_raises_error(self):
        self.assertRaises(TypeError,AbstractHasher)


    #just for getting the hang of test driven development

    def test_md5_hash(self):
        hash = self.hasher.getHash(self.data)
        self.assertEqual(hash,b'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9')







if __name__=="__main__":
    unittest.main()

