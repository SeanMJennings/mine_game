from src.domain.board import Board
from src.domain.player import Player
board = None

def a_board(*args):
    global board
    board = Board(Player(1,1), (4,4))
def moving_a_player(movement):
    board.move_player(movement)
def a_board_of_size(width, height):
    global board
    board = Board(Player(1,1), (width, height))
def a_player_moves_to(position):
    _a_player_moves_to(position)
def _a_player_moves_to(position):
    player = board.get_player()
    assert player.x == position[0]
    assert player.y == position[1]