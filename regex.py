import re


pattern = re.compile('^dog$')
print pattern.match('dog')
print pattern.match('xdog')

