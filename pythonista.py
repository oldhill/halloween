""" http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
"""

person = ['David', 'Pythonista', 'Some number']
person2 = ['Guido', 'BDFL', 'Some other number']

for name, title, phone_number in [person, person2]:
  print '%s, %s at %s' % (name, title, phone_number)

