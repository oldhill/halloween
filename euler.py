n = 100000000;
print '\nFinding sum of multiples of 3 and 5 below %d' % n

total = 0;
for i in xrange(0, n):
  if i % 3 == 0 or i % 5 == 0:
    total += i

print 'Result: %d' % total
