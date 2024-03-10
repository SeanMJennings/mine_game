from enum import Enum
from .player import Player

class Direction(Enum):
  UP = 'up',
  DOWN = 'down',

class Board:
  def __init__(self, player : Player):
    self._player = player
  def move_player(self, direction : Direction):
    direction = Direction[direction.upper()]
    match direction:
      case Direction.UP:
        self._player.y += 1      
      case Direction.DOWN:
        self._player.y -= 1
  def get_player(self):
    return self._player