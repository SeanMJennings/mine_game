from src.domain.board import Board
from src.domain.player import Player
board = None

def a_board(*args):
    global board
    board = Board(Player(1,1))
def moving_a_player(movement):
    board.move_player(movement)
def a_player_moves(position):
    _a_player_moves(position)
def _a_player_moves(position):
    player = board.get_player()
    assert player.x == position[0]
    assert player.y == position[1]