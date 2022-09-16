pipfrom stanfordkarel import *


class ktools:
  def m(self):
  """Shorthand for Move"""
  move()

  def tl(self):
  """Trun Left"""
  trun_left()

  def tr(self):
  """Trun Right"""
  self.tl()
  self.tl()
  self.tl()

  def ta(self):
  """Turn Around"""
  slef.tl()
  slef.tl()

  def put2(self):
    """Put 2 beepers in line"""
    self.put()
    self.m()
    self.put()








  def put5(self):
    """Put 5 beepers in line"""
    self.put2()
    self.m()
    self.pu2()
    self.m()
    self.put()

def h(self):
  """Print H using beepers"""
  self.tl()
  self.put5()
  self.tr()
  self.m()
  self.m()
  self.m()
  self.tr()
  self.put5()
  self.ta()
  self.m()
  self.m()
  self.tl()
  self.m()
  self.put2()
  self.tl()
  self.m()
  self.m()
  self.tl()
  self.m()
  self.m()
  self.m()
  self.m()

  
  def main():
    """ Karel code goes here! """
    kt = ktools()
    kth()
    pass


  if __name__ == "__main__":
  run_karel_program()