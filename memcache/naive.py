import datetime


class Memcache():
  """ Naive 100 item LRU in-memory k/v cache """
  def __init__(self, size=100):
    self.size = size
    self.items = {}

  def get(self, k):
    """ Get value and update accessed time """
    v = self.items.get(k)
    if v:
      self.items[k]['accessed'] = datetime.datetime.utcnow()
    return v

  def set(self, new_key, new_val):
    """ Set value and evict LRU item if necessary """

    if len(self.items) >= self.size:
      lru_time = datetime.datetime.utcnow()
      oldest_key = None
      for k, v in self.items.iteritems():
        if v['accessed'] < lru_time:
          lru_time = v['accessed']
          oldest_key = k
      print 'Evicting LRU key %s to maintain size %s' % (oldest_key, self.size)
      self.items.pop(oldest_key)

    self.items[new_key] = {
      'value': new_val,
      'accessed': datetime.datetime.utcnow()
    }

    return self.items
