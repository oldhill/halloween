import random
import time

DELAY = 10

while 1:
  time.sleep(DELAY)
  useful_powers_of_2 = {7, 8, 10, 16, 20, 30, 32, 40}
  random_power_of_2 = random.sample(useful_powers_of_2, 1)[0]
  print '\nWhat\'s the largest %s bit integer?' % random_power_of_2

  time.sleep(DELAY)
  print 'Answer: %s' % '{:,}'.format(2 ** random_power_of_2)