__author__ = 'girish'
import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description="reverse hashes of passwords")
    parser.add_argument('hash',type=str,help="The hash you want to reverse")
    algorithm_group = parser.add_mutually_exclusive_group(required=True)
    algorithm_group.add_argument("--md5",action="store_true",default=False)
    algorithm_group.add_argument("--sha1",action="store_true",default=False)
    algorithm_group.add_argument("--sha256",action="store_true",default=False)

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-n","--num",metavar='N',type=int,help="only use number having N length")
    input_group.add_argument("-c","--chars",metavar="N",type=int,help="only use characters having N length")
    input_group.add_argument("-b","--both",metavar="N",type=int,help="use both having N length")
    input_group.add_argument("-r","--regex",metavar="N",type=str,help="use a regex for the desired query set (beta) ")

    return parser.parse_args(args)


