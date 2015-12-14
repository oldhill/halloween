# NOTE this is not real production code and isn't used in any applications.
# Never roll yr own crypto! use bcrypt/scrypt/other! etc
# https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet
# https://security.stackexchange.com/questions/17421/how-to-store-salt
# Just some explorations of python hashing functions etc...


from pprint import pprint

# Using system csprng via SystemRandom builtin, since default random generator
# is Mersenne Twister, which is not cryptographically secure b/c it's deterministic.
import random
csprng = random.SystemRandom()
print csprng.choice('abcdefg')
print csprng.random()
print ''


# Hash some stuff!
import hashlib

# construct rainbow table of unsalted pw hashes
rainbow_table = {}
for pw in ('password', '1234', 'correct horse battery staple'):
  rainbow_table[hashlib.sha256(pw).hexdigest()] = pw

pprint(rainbow_table)
# it works! verified via $ echo -n "correct horse battery staple" | openssl dgst -sha256
print ''

# unsalted and salted 'user dbs'
from collections import namedtuple

Usr = namedtuple('User', ['pw', 'salt'])

unsalted_db = [
  Usr(pw=hashlib.sha256('password').hexdigest(), salt=None),
  Usr(pw=hashlib.sha256('1234').hexdigest(), salt=None),
]

salted_db = [
  Usr(pw=hashlib.sha256('password' + 'salt1').hexdigest(), salt='salt1'),
  Usr(pw=hashlib.sha256('1234' + 'salt2').hexdigest(), salt='salt2'),
]

pprint(unsalted_db)
print ''
pprint(salted_db)

# get 'cracking'

def crack(pw_hash):
  """ crack or throw error KeyError """
  return rainbow_table[pw_hash]

print 'Unsalted:'
for usr in unsalted_db:
  try:
    print crack(usr.pw)
  except KeyError:
    print 'couldn\'t crack!'

print '\nSalted:'
for usr in salted_db:
  try:
    print crack(usr.pw)
  except KeyError:
    print 'couldn\'t crack!'

print 'yea but you could generate individual rainbow tables with each user\'s salt...\n'

# what about profiling hash functions TODO actually implement this
import cProfile
# pw = 'this is some fairly long string of words yeah still going it\'s really long'
# cProfile.run(hashlib.sha1(pw).hexdigest())
# print ''
# cProfile.run(hashlib.sha256(pw).hexdigest())
# print ''
# cProfile.run(hashlib.sha512(pw).hexdigest())
# print ''
