import time
import unittest

import naive


class TestNaiveMemcache(unittest.TestCase):

  def test_get_set(self):
    m = naive.Memcache()
    m.set('hi', 'there')
    self.assertEqual('there', m.get('hi')['value'])

  def test_lru_eviction(self):
    m = naive.Memcache(size=5)
    m.set('hi', 'there')
    self.assertEqual('there', m.get('hi')['value'])
    time.sleep(2)
    for i in xrange(5):
      m.set(i, i + 1)
    self.assertIsNone(m.get('hi'))
    self.assertEqual(5, len(m.items))

if __name__ == '__main__':
  unittest.main()
