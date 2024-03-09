from enum import Enum
from .player import Player

class Board:
  def __init__(self):
    self.player = Player()
  def move_player(self, direction):
    match direction.lower():
      case Direction.Up:
        self.player.y += 1      
      case Direction.Down:
        self.player.y -= 1
  def get_player(self):
    return self.player
  
class Direction(Enum):
  Up = 'up',
  Down = 'down',