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

# Other languages have "variables"
print ''
a = 2
b = 2
print 'Memory addresses of those names: %s, %s' % (hex(id(a)), hex(id(a)))

# Default parameter values
print ''

def bad_append(new_item, a_list=[]):
  """ a_list is initialized at function definition time... uh oh... """
  a_list.append(new_item)
  return a_list

print bad_append('one')
print bad_append('two')

# Advanced % string formatting
print ''
from pprint import pprint
print 'Locals: '
pprint(locals())
print '\nGlobals: '
pprint(globals())

# List comps
print ''
print [n ** 2 for n in xrange(10)]
print [n ** 2 for n in xrange(10) if n % 2]

# Generator expressions (1)
total = 0
for num in range(1, 101):
  total += num * num
print 'looped: %i' % total

print 'lc: %i' % sum([num * num for num in range(1, 101)])

print 'genexp: %i' % sum(num * num for num in xrange(1, 101))

print 'genexp lazy eval:'
my_genexp = (num * num for num in xrange(1, 101))
print my_genexp
for i in xrange(1, 5):
  print my_genexp.next()

# Sorting with keys
print ''
my_list = ['hi', 'there', 'x', 'z', 'longword', 'bye']
my_list.sort(key=len)
print my_list
my_list.sort(key=str.lower)  # alphabetically regardless of case
print my_list

# Generators full stop
print ''
def my_range_generator(stop):
  v = 0
  while v < stop:
    yield v
    v += 1

print 'Generated ints w conditional stop:'
for i in my_range_generator(5):
  print i

def my_other_range_generator(stop):
  v = 0
  while 1:
    yield v
    v += 1
    if v == stop:
      raise StopIteration

print '\nGenerated ints w StopIteration raise:'
for i in my_other_range_generator(5):
  print i
