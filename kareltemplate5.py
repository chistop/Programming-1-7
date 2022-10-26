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

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()
    
  def put(self):
    """Put beeper"""
    put_beeper()

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

  def C(self):
    """Print H using beepers"""
    self.putm(3)
    self.ta()
    self.mm(2)
    self.tr()
    self.m()
    self.putm(4)
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.mm(4)
    self.tl()
    self.mm(2)

  def R(self):
    """print R using beepers"""
    self.tl()
    self.putm(4)
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.mm(2)

  def I(self):
    """Print I using beepers"""
    self.putm(3)
    self.ta()
    self.m()
    self.tl()
    self.m()
    self.putm(4)
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.mm(2)
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.mm(4)
    self.tl()
    self.mm(3)

  def S(self):
    """Print S using beepers"""
    self.putm(3)
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.putm(3)
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.putm(3)

  def e(self):
    """Print E using beepers"""
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tl()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.mm(5)
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.mm(4)
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.m()

  def O(self):
    """Print O using deepers"""
    self.put3()
    self.m()
    self.tr()
    self.put4()
    self.m()
    self.tr()
    self.put3()
    self.m()
    self.tl()
    self.put4()
    self.m()
    self.tr()
    self.mm(4)

  def T(self):
    """Print T using beepers"""
    self.tl()
    self.putm(4)
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.tr()
    self.putm(3)
    self.tr()
    self.mm(4)
    self.tl()
    self.mm(2)
    

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
      
  def mm(self, num):
    """Move Multiple"""
    for number in range(0, num):
      self.m()
    
  def putm(self, num):
    """Put multiple"""
    for i in range(num - 1):
      self.put()
      self.m()
    self.put()
  
  def pickm(self, num):
    """pick Multiple"""
    for _ in range(num - 1):
      self.pick()
      self.m()
      self.pick()
      
  def SOB(self, num):
    """Standing on Beeper"""
    return beepers_present()
    
  def jump(self):
    """Jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()
  
  def find(self):
    """Find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
    pass


    
def main():
    """ Karel code goes here! """
    kt = ktools()
    pass


if __name__ == "__main__":
    run_karel_program()