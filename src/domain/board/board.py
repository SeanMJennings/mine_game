from .direction import Direction
from ..player import Player
from .mine_generator import MineGenerator

class Board:
  
  def __init__(self, player: Player, dimensions: tuple[int,int], mine_generator: MineGenerator):
    self._player = player
    self._dimensions = dimensions
    self._mines = mine_generator.generate_mines()
    
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
    self.check_for_mine()

  def __inside_right_of_board(self):
      return self._player.x + 1 <= self._dimensions[0] - 1

  def __inside_left_of_board(self):
      return self._player.x - 1 >= 0

  def __inside_bottom_of_board(self):
      return self._player.y - 1 >= 0

  def __inside_top_of_board(self):
      return self._player.y + 1 <= self._dimensions[1] - 1
    
  def check_for_mine(self):
    mine = list(filter(lambda mine: mine.position[0] == self._player.x and mine.position[1] == self._player.y, self._mines))
    if (len(mine) == 1):
      self._player.mine_hit()
    
  def get_player(self):
    return self._player