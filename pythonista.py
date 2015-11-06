""" http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
"""

import collections


# Unpacking right hand operand to left hand tuple
print ''
person = ['David', 'Pythonista', 'Some number']
person2 = ['Guido', 'BDFL', 'Some other number']

for name, title, phone_number in [person, person2]:
  print '%s, %s at %s' % (name, title, phone_number)

# Building strings
print ''
colors = ['red', 'blue', 'green', 'yellow']
print 'Comma separated: %s' % ','.join(colors)
print 'W/ slicing: %s or %s' % (', '.join(colors[:-1]), colors[-1])

def uppercase_first_letter(my_string):
  return my_string[0].upper() + my_string[1:]
print 'Uppercased: %s' % ', '.join(uppercase_first_letter(i) for i in colors)

# Gonna use this for various dictionary stuff
STUFF = [
  ('keyboards', 5),
  ('keyboards', 10),
  ('mice', 1),
  ('mice', 1),
  ('laptops', 3),
]

# Dictionary get method
print ''
stuff_counts = {}
for (thing, count) in STUFF:
  stuff_counts[thing] = stuff_counts.get(thing, 0) + count
print 'Stuff counts: %s' % stuff_counts

# Dictionary setdefault method
print ''
grouped_stuff = {}
for (thing, count) in STUFF:
  group = grouped_stuff.setdefault(thing, [])
  group.append(count)
print 'Grouped stuff: %s' % grouped_stuff

# defaultdict
print ''
stuff_counts = collections.defaultdict(int)
for (thing, count) in STUFF:
  stuff_counts[thing] += count
print 'Stuff counts: %s' % stuff_counts

print ''
grouped_stuff = collections.defaultdict(list)
for (thing, count) in STUFF:
  grouped_stuff[thing].append(count)
print 'Grouped stuff: %s' % grouped_stuff

# Zipping up iterables
print ''
given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']
print zip(given, family)

# Enumerate is a generator
print ''
items = 'zero one two three'.split()
e = enumerate(items)
print 'Enumerate generator mem address: %s' % e
print 'Is that same as the CPython id in hex (mem address?) %s' % hex(id(e))
print '\nOK let\'s iterate a couple times:'
print e.next()
print e.next()

# Start here: Other languages have "variables"
print ''
