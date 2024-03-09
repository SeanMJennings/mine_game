from enum import Enum
from .player import Player

class Board:
  def __init__(self):
    self.player = Player()
  def move_player(self, direction):
    direction = Direction[direction.upper()]
    match direction:
      case Direction.UP:
        self.player.y += 1      
      case Direction.DOWN:
        self.player.y -= 1
  def get_player(self):
    return self.player
  
class Direction(Enum):
  UP = 'up',
  DOWN = 'down',