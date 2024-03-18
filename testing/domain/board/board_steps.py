from src.domain.board.board import Board
from src.domain.player import Player
from testing.domain.board.fakes.fake_mine_generator import FakeMineGenerator
board = None
player = None

def a_player_in_position(position):
    global player
    player = Player(position)
def moving_a_player(movement):
    board.move_player(movement)
def a_board_of_size(dimensions: tuple[int,int]):
    global board
    global player
    board = Board(player, dimensions, FakeMineGenerator(False, dimensions))
def a_board_full_of_mines_with_size(dimensions: tuple[int,int]):
    global board, player
    board = Board(player, dimensions, FakeMineGenerator(True, dimensions))
def a_player_moves_to(position):
    _a_player_moves_to(position)
def _a_player_moves_to(position):
    player = board.get_player()
    assert player.x == position[0]
    assert player.y == position[1]
def a_player_detonates_a_mine(*args):
    assert player.mines_detonated == 1
def the_mine_only_detonates_once(*args):
    a_player_detonates_a_mine()