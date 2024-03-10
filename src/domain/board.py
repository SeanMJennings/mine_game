from enum import Enum
from .player import Player

class Direction(Enum):
  up = 'up',
  down = 'down',
  left = 'left',
  right = 'right'

class Board:
  def __init__(self, player : Player):
    self._player = player
  def move_player(self, direction : Direction):
    direction = Direction[direction.lower()]
    match direction:
      case Direction.up:
        self._player.y += 1      
      case Direction.down:
        self._player.y -= 1      
      case Direction.left:
        self._player.x -= 1      
      case Direction.right:
        self._player.x += 1
  def get_player(self):
    return self._player