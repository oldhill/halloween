

SIZES = {'small', 'medium', 'insanely massive'}


class PhysicalThing(object):
  """ Base class for physical object
  """
  def __init__(self, *args, **kwargs):
    """ Validate and set attrs
    """
    size = kwargs.pop('size', None)
    if size and size not in SIZES:
      raise ValueError('Invalid size!')
    self.size = size

    weight = kwargs.pop('weight', 0)
    if weight and weight < 0:
      raise ValueError('Weight can\'t be negative!')
    self.weight = weight


class Electronic(PhysicalThing):
  """ Yeah
  """
  def beep(self):
    specific_attr_vals = [self.__getattribute__(n) for n in {'size', 'weight'}]
    print ('Bleep bloop here are some attr values: %s' %
           [v for v in specific_attr_vals if v])


class Computer(PhysicalThing):
  """ It's computers
  """
  def __init__(self, *args, **kwargs):
    self.os = kwargs.pop('os', 'Linux is the default!')
    super(Computer, self).__init__(self, *args, **kwargs)


class Laptop(Electronic, Computer):
  """ Aye
  """
  @staticmethod
  def yo():
    print 'Yo.'
