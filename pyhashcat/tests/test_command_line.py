__author__ = 'girish'

import unittest
import cli

class commandLineTest(unittest.TestCase):


    def test_algorithm_group(self):


        self.assertEqual(cli.parse_args(["--sha1","-c","6","hash"]).sha1,True)


    def test_character_group(self):

        self.assertEqual(cli.parse_args(["--sha1","-c","6","hash"]).chars,6)

    def test_no_algorithm_group(self):
        try:

            self.assertRaises(cli.parse_args(["hash"]),lambda :SystemExit)
        except SystemExit:
            self.assertEqual(True,True) #cant find other way to check system exit

