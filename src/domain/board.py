from .direction import Direction
from .player import Player

class Board:
  
  def __init__(self, player: Player, dimensions: tuple[int,int]):
    self._player = player
    self._dimensions = dimensions
    
  def move_player(self, direction: Direction):
    direction = Direction[direction.lower()]
    match direction:
      case Direction.up:
        if (self.__inside_top_of_board()):
          self._player.move(direction)  
      case Direction.down:
        if (self.__inside_bottom_of_board()):
          self._player.move(direction)      
      case Direction.left:
        if (self.__inside_left_of_board()):
          self._player.move(direction)     
      case Direction.right:
        if (self.__inside_right_of_board()):
          self._player.move(direction)

  def __inside_right_of_board(self):
      return self._player.x + 1 <= self._dimensions[0] - 1

  def __inside_left_of_board(self):
      return self._player.x - 1 >= 0

  def __inside_bottom_of_board(self):
      return self._player.y - 1 >= 0

  def __inside_top_of_board(self):
      return self._player.y + 1 <= self._dimensions[1] - 1
    
  def get_player(self):
    return self._player