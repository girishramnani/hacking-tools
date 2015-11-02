__author__ = 'girish'
import argparse

def parse_args(args):
    parser = argparse.ArgumentParser(description="reverse hashes of passwords")
    parser.add_argument('--hash',type=str,help="The hash you want to reverse",required=True)
    algorithm_group = parser.add_mutually_exclusive_group(required=True)
    help_s = "Use the {} hashing algorithm"

    algorithm_group.add_argument("--md5",action="store_true",default=False,help=help_s.format("md5"))
    algorithm_group.add_argument("--sha1",action="store_true",default=False,help=help_s.format("sha1"))
    algorithm_group.add_argument("--sha256",action="store_true",default=False,help=help_s.format("sha256"))

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-n","--num",metavar='N',type=int,help="only use number having N length")
    input_group.add_argument("-c","--chars",metavar="N",type=int,help="only use characters having N length")
    input_group.add_argument("-b","--both",metavar="N",type=int,help="use both having N length")
    input_group.add_argument("-r","--regex",metavar="N",type=str,help="use a regex for the desired query set (beta) ")

    parser.add_argument("-v","--verbose",action="store_true",default=False)

    return parser.parse_args(args)


