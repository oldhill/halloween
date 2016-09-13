"""Livin life, doin stuff """


import argparse


parser = argparse.ArgumentParser()

parser.add_argument('search_string',
                    help='string to grep for')

parser.add_argument('--sys',
                    help='shell out to system grep',
                    action='store_true')


all_args = parser.parse_args()

print 'Here is the positional arg you entered: %s' % all_args.echo



