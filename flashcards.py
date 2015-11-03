import os
import random
import time

DELAY = 10

while 1:
  time.sleep(DELAY)
  os.system('clear')
  useful_powers_of_2 = {7, 8, 10, 16, 20, 30, 32, 40}
  approx = {10: '1 thousand',
            20: '1 million',
            30: '1 billion',
            40: '1 trillion'}

  random_power_of_2 = random.sample(useful_powers_of_2, 1)[0]
  print '\nWhat\'s the largest %s bit integer?' % random_power_of_2

  time.sleep(DELAY)
  print 'Answer: %s - 1' % '{:,}'.format(2 ** random_power_of_2)
  print 'Approx: %s' % approx.get(random_power_of_2, 'nothin in particular')
