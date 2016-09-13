"""
Command line 'tool' to search for strings :)

Danger: use at your own risk!

Written just for fun.
"""


import argparse
import os
import sys


def main():
    parser = setup_parser()
    args = parser.parse_args()

    print 'About to search for: %s' % args.term

    if not args.target:
        print ('Sorry, have not yet implemented untargeted grep. '
               'Plz try running with --target argument.')
        sys.exit(0)

    print 'Targeting this file: %s' % args.target

    if args.system:
        print 'Shelling out to system grep...'
        # TODO: something like os.system('grep %s' % args.target)

    else:
        print 'Using python instead of system grep.\n\nResults:'
        with open(args.target, 'r') as infile:
            line_number = 1
            for l in infile:
                if args.term in l:
                    print '%s: %s' % (line_number, l)
                line_number += 1


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('term',
                        help='search term to grep for')
    parser.add_argument('--system',
                        help='shell out to system grep',
                        action='store_true')
    parser.add_argument('--target',
                        help='target file to search within')
    return parser


if __name__ == '__main__':
    main()
