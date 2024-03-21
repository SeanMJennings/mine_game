# from src.application.mine_game import MineGame
# from src.domain.board.board import Board
# from src.domain.player import Player
# from testing.domain.board.fakes.fake_mine_generator import FakeMineGenerator

# mine_game = None
# board = None
# game_overview = None

# def a_game_with_no_mines(*args):
#     global mine_game, board
#     board = Board(Player((0,0)), (8,8), FakeMineGenerator(False, (8,8)))
#     mine_game = MineGame(board)
    
# def requesting_game_overview(*args):
#     global mine_game, game_overview
#     game_overview = mine_game.GetOverview()

# def the_overview_is_returned(*args):
#     global game_overview
#     assert game_overview.Status == "InPlay"