#!/usr/bin/python

"""rename.py - regex batch file renamer

Inspired by Larry Wall's filename fixer perl script:
        The Perl Coookbook,
        Chapter 9.9, Renaming Files
        O'Reilly, 1999

Synopsis:
    rename.py [options] <pattern> <replacement> [<file1> ... <fileN>]

    Options:
        --help  This help documentations.
        --doit  Rename files. The default behaviour is to print what
                would be done.

Examples:

    # Print what would be done to rename all avi files to just show name and episode string.
    rename.py '.*(S\d\dE\d\d).*' 'Quantico - \1.avi' *.avi

    # Perform the rename.
    rename.py '.*(S\d\dE\d\d).*' 'Quantico - \1.avi' *.avi --doit

Licence:

Copyright 2015 Dave Webb

rename.py is free software. You can do *anything* you like with it.
"""

import getopt
import re
import shutil
import sys

def main(argv):
    doit = False

    try:
        opts, args = getopt.gnu_getopt(argv, "hd", ["help", "doit"])
    except getopt.GetoptError:
        usage(getopt.GetoptError)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage("")
        elif opt in ("-d", "--doit"):
            doit = True

    if len(args) < 3:
        usage("Please supply <pattern> and <replacement>")

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
        print
    print __doc__
    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
