#!/usr/bin/python

import getopt
import re
import shutil
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

    if len(args) < 3:
        usage("")
        sys.exit(2)

    pattern = args.pop(0)
    sub     = args.pop(0)

    for infile in args:
        outfile = re.sub(pattern, sub, infile)
        if infile == outfile:
            print "No change to " + infile
        else:
            print infile + "  -->  " + outfile
            if doit:
                shutil.move(infile, outfile)

def usage(msg):
    if msg:
        print msg
    print "USAGE: rename.py <pattern> <replacement> <files> [--doit]"

if __name__ == "__main__":
    main(sys.argv[1:])
