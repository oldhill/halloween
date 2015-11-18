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



                Check out https://python.org/ for more info!

                Some more URLs: http://miniramp.net/
                                https://google.com/
                                https://google.coormg/

                Best,
                Y
            """

# http/s URLs
pattern = re.compile('http[s]*[:]+[/.a-z]+/')
print re.findall(pattern, my_string)

# TODO(oldhill) return to this someday and fix this mess
# .com, .org, but not .net (or .coormg)
print ''
pattern = re.compile('http(?=([:/a-z]+.(com|org)))')  # still not right...
print re.findall(pattern, my_string)

# split on two or more newlines
print ''
split_string = re.split('[\n+]{2,}', my_string)
for i in split_string:
  print 'Group: %s' % i.strip()

# (wip) dispatch a 'request' to route to a matching handler
print ''
def dispatch(url):
  dispatcher = [
    ('^[a-z]+$', 'just_some_letters'),
    ('^[0-9]+$', 'just_some_numbers'),
    ('^/account/{0,1}$', 'accounts'),
    ('^/account/[0-9]+$', 'specific_account'),
    # Not quite right, needs to support URL encoding w/ %
    ('^/account/[0-9]+\?[a-zA-Z_]+=[a-zA-Z0-9_]+$',
     'specific_account_with_query_param'),
  ]
  for pattern, handler in dispatcher:
    if re.match(pattern, url):
      return handler
  return '404 :D'

print 'Do the \'tests\' pass?'
print dispatch('hi') == 'just_some_letters'
print dispatch('123') == 'just_some_numbers'
print dispatch('hi123') == '404 :D'
print dispatch('/account') == 'accounts'
print dispatch('/account/') == 'accounts'
print dispatch('/account/123') == 'specific_account'
print dispatch('/account/123abc') == '404 :D'
print (dispatch('/account/123?some_para=hi123')
       == 'specific_account_with_query_param')
print dispatch('/account/123??some_para=hi123') == '404 :D'