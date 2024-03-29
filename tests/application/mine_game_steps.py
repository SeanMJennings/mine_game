from mine_game.application.mine_game import MineGame
from mine_game.application.game_status import GameStatus
from mine_game.domain.board.board import Board
from mine_game.domain.player import Player
from mine_game.domain.board.direction import Direction
from tests.domain.board.fakes.fake_mine_generator import FakeMineGenerator

mine_game = None
board = None
game_overview = None


def a_game_with_no_mines(*args):
    global mine_game, board
    board = Board(Player((0, 0)), (8, 8), FakeMineGenerator(False, (8, 8)))
    mine_game = MineGame(board)


def a_game_with_mines(*args):
    global mine_game, board
    board = Board(Player((0, 0)), (8, 8), FakeMineGenerator(True, (8, 8)))
    mine_game = MineGame(board)


def requesting_game_overview(*args):
    global mine_game, game_overview
    game_overview = mine_game.get_overview()


def the_overview_is_returned(*args):
    global game_overview
    assert game_overview.game_status == GameStatus.Active
    assert game_overview.player_position == (0, 0)
    assert game_overview.mines_detonated == 0


def moving_up_three_spaces(*args):
    global mine_game
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)


def moving_to_top_of_board(*args):
    global mine_game
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)
    mine_game.move(Direction.up)


def the_game_is_lost(*args):
    global mine_game, game_overview
    game_overview = mine_game.get_overview()
    assert game_overview.game_status == GameStatus.Lost
    assert game_overview.mines_detonated == 3
    assert game_overview.player_position == (0, 3)


def the_game_is_won(*args):
    global mine_game, game_overview
    game_overview = mine_game.get_overview()
    assert game_overview.game_status == GameStatus.Won
    assert game_overview.mines_detonated == 0
    assert game_overview.player_position == (0, 7)


def game_is_lost(*args):
    a_game_with_mines()
    moving_up_three_spaces()


def game_is_won(*args):
    a_game_with_no_mines()
    moving_to_top_of_board()


def trying_to_move_player_down(*args):
    global mine_game
    mine_game.move(Direction.down)


def dead_player_does_not_move(*args):
    global mine_game, game_overview
    game_overview = mine_game.get_overview()
    assert game_overview.player_position == (0, 3)


def alive_player_does_not_move(*args):
    global mine_game, game_overview
    game_overview = mine_game.get_overview()
    assert game_overview.player_position == (0, 7)
