"""Livin life, doin stuff """


import argparse


parser = argparse.ArgumentParser()

parser.add_argument('term',
                    help='search term to grep for')

parser.add_argument('--system',
                    help='shell out to system grep',
                    action='store_true')


args = parser.parse_args()

print 'OK going to grep the current directory for %s.' % args.term
if args.system:
    print 'shelling out to system grep'
else:
    print 'using python instead of system grep'
