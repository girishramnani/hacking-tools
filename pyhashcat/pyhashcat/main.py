__author__ = 'girish'


import sys
import cli
import keyGenerator
import Hasher

def choose_key_generator(arguments):

    if arguments.chars :
        key_generator = keyGenerator.CharacterGenerator(arguments.chars)
    elif arguments.num :
        key_generator = keyGenerator.NumericGenerator(arguments.num)
    elif arguments.both :
        key_generator = keyGenerator.allSymbolGenerator(arguments.both)

    return key_generator


def choose_hasher(arguments):
    if arguments.md5:
        hasher = Hasher.MD5Hasher()
    elif arguments.sha1:
        hasher = Hasher.SHA1Hasher()
    elif arguments.sha256 :
        hasher = Hasher.SHA256Hasher()

    return hasher


if __name__=="__main__":
    arguments = cli.parse_args(sys.argv)
    hasher = choose_hasher(arguments)
    key_generator = choose_key_generator(arguments)

    desired_hash = arguments.hash

    for key in key_generator.gen_keywords():
        if arguments.verbose :
            print("comparing {key} ".format(key=key))


