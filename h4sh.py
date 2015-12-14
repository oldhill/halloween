# NOTE this is not real production crypto code and isn't used in any applications.
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
  rainbow_table[pw] = hashlib.sha256(pw).hexdigest()

pprint(rainbow_table)





