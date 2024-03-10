from src.domain.board import Board
from src.domain.player import Player
board = None

def a_board():
    board = Board(Player(1,1))
def moving_a_player(movement):
    board.move_player(movement)
def a_player_moves(position):
    position = board.get_player()
    assert position.x == position[0]
    assert position.y == position[1]