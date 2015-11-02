__author__ = 'girish'

import unittest
import cli

class commandLineTest(unittest.TestCase):


    def test_algorithm_group(self):
        parser = cli.parse_args()

        self.assertEqual(parser.parse_args(["--sha1","hash"]).sha1,True)


    def test_no_algorithm_group(self):
        parser = cli.parse_args()
        try:

            self.assertRaises(parser.parse_args(["hash"]),lambda :SystemExit)
        except SystemExit:
            self.assertEqual(True,True) #cant find other way to check system exit

