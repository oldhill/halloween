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


# Finding all matches
print ''
pattern = re.compile('[a-z]+@[a-z]+\.com')
search_results = pattern.findall('---foo@bar.com---()*jdjhgjdh&&66x@y.com***')
print search_results

# Multi-line strings
print ''
my_string = """ Dear X,

                Hi! Have you tried coding in Python? It's
                pretty cool. Very fun to work with and expressive,
                although the dynamic type system can wreak havoc in
                large codebases. Highly recommended!

                Check out https://www.python.org/ for more info!

                Some more URLs: http://miniramp.net/
                                https://google.com/

                Best,
                Y
            """
# http/s URLs
pattern = re.compile('http[s]*[:]+[/.a-z]+/')
print re.findall(pattern, my_string)

# .com, .org, but not .net
pattern = re.compile('http[s]*[:]+[/.a-z]+[com|org]/')  # not quite right... shouldn't be a char group
print re.findall(pattern, my_string)