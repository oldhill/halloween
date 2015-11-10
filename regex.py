""" Now you have two problems

https://docs.python.org/2/library/re.html

https://docs.python.org/2/howto/regex.html
"""

import re


# Exact string match
pattern = re.compile('^dog$')
print pattern.match('dog')
print pattern.match('xdog')


# Basic .com email address
print ''
pattern = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$')
print pattern.match('x@y.com')
print pattern.match('@y.com')
print pattern.match('x@y.')
print pattern.match('&x@y.com*---')


# Find email address w/in larger string
print ''
pattern = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com')
print pattern.search('x@y.com')
print pattern.search('@y.com')
print pattern.search('x@y.')
print pattern.search('&x@y.com*---')
print pattern.match('&x@y.com*---')  # not exact match

print ''
print 'parsing it out:'
search_results = pattern.search('&x@y.com*---')
print dir(search_results)
print search_results.group(0)
