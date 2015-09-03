__author__ = 'girish'
from unittest import TestCase
import unittest



class standard_hash_test(object):

    def __init__(self,Algorithm):
        self.algorithm = Algorithm


    def test_small_hash_compare(self):
        pass


    def test_all_number_hash_compare(self):
        pass

    def test_all_alphabet_hash_compare(self):
        pass


    def test_all_special_charactor_hash_compare(self):
        pass


from pyhashcat.Hasher import AbstractHasher

class hasher_test(TestCase):


    def setUp(self):
        self.data = "hello_world"

    def test_if_abstract_hasher_raises_error(self):
        self.assertRaises(TypeError,AbstractHasher)


    #just for getting the hang of test driven development
    def test_algorithm_prop(self):
        pass


if __name__=="__main__":
    unittest.main()

