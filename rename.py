#!/usr/bin/python

r"""rename.py - regex batch file renamer

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

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

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
