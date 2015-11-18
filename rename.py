#!/usr/bin/python

import getopt
import sys

def main(argv):
    doit = False

    try:
        opts, args = getopt.gnu_getopt(argv, "hd", ["help", "doit"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage("")
            sys.exit()
        elif opt in ("-d", "--doit"):
            doit = True
        elif opt == "--doit":
            doit = True

    pattern = args.pop(0)

def usage(msg):
    if msg:
        print msg
    print "USAGE: rename.py <regex> <files> [--doit]"

if __name__ == "__main__":
    main(sys.argv[1:])
