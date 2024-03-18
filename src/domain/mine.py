class Mine:
  
  def __init__(self, position: tuple[int,int]):
    self._position = position
    self._detonated = False
    
  @property
  def position(self):
    return self._position
  
  @property
  def detonated(self):
    return self._detonated
  
  def detonate(self):
    self._detonated = True
      