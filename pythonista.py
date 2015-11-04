""" http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
"""

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

# Dictionary get method
print ''
# TODO
