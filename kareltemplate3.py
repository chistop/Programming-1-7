from stanfordkarel import *


class ktools:

  def m(self):
    """Shorthand for Move"""
    move()

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def put(self):
    """Put beeper"""
    put_beeper()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

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

  def fic(self):
    """Front is Clear"""
    return front_is_clear

  def fib(self) ->bool:
    """Front is Block"""
    return not self.fib()

  def ric(self) ->bool:
    """Right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return True
    self.tl()
    return False

  def rib(self) ->bool:
    """Right is Block"""
    return not self.ric()

def mazemove(self):
  """Maze Move"""
  if self.fib():
    self.tl()
  else:
    self.m()
    if self.ric():
      self.tr()
      self.m()
      if self.ric():
        self.tr()
        self.m()
      pass      
  
  

def main():
    """ Karel code goes here! """
    
    pass


if __name__ == "__main__":
    run_karel_program()
