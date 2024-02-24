from .player import Player

class Board:
  def __init__(self):
    self.player = Player()
  def move_player(self, direction):
    self.player.y = 1
  def get_player(self):
    return self.player