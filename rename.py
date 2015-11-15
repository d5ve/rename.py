#!/usr/bin/python

import getopt
import sys

for arg in sys.argv:
    print arg

def main(argv):
    doit = False

    try:
        opts, args = getopt.getopt(argv, "hd", ["help", "doit"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

def usage(msg):
    if msg:
        print msg
    print "USAGE: rename.py <regex[s]> <files> [--doit]"
 
if __name__ == "__main__":
    main(sys.argv[1:])
