__author__ = 'girish'

import time
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
    arguments = cli.parse_args(sys.argv[1:]) # removing the filename
    hasher = choose_hasher(arguments)
    key_generator = choose_key_generator(arguments)

    desired_hash = arguments.hash

    #matric
    init_time = time.time()
    keys=0


    for key in key_generator.gen_keywords():


        joined_key = "".join(key)
        output_hash = hasher.getHash(joined_key,True)
        keys+=1

        if arguments.verbose :
            print("comparing {key} as {hash} with {d_hash}".format(key=joined_key,hash=output_hash,d_hash= desired_hash))


        if output_hash == desired_hash :
            print()
            print("The key you are looking for is {}".format(joined_key))
            break
    else:
        print("The key for the desired hash wasnt found")
    total_time =time.time() -init_time
    print()
    print("Time elapsed : {} s".format(total_time) )
    print("Keys compared : {} ".format(keys))
    print("Keys per second : {}".format(keys/(total_time)))


