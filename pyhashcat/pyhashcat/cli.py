__author__ = 'girish'
import argparse

def parse_args(args=[]):
    parser = argparse.ArgumentParser(description="reverse hashes of passwords")
    parser.add_argument('hash',type=str,help="The hash you want to reverse")
    algorithm_group = parser.add_mutually_exclusive_group(required=True)
    algorithm_group.add_argument("--md5",action="store_true",default=False)
    algorithm_group.add_argument("--sha1",action="store_true",default=False)
    algorithm_group.add_argument("--sha256",action="store_true",default=False)




    return parser

