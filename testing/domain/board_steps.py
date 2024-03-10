from src.domain.board import Board
from src.domain.player import Player
board = None
player = None

def a_player_in_position(position):
    global player
    player = Player(position)
def a_board(*args):
    global board
    board = Board(player, (4,4))
def moving_a_player(movement):
    board.move_player(movement)
def a_board_of_size(dimensions: tuple[int,int]):
    global board
    global player
    board = Board(player, dimensions)
def a_player_moves_to(position):
    _a_player_moves_to(position)
def _a_player_moves_to(position):
    player = board.get_player()
    assert player.x == position[0]
    assert player.y == position[1]