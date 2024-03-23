from mine_game.domain.board.board import Board
from mine_game.domain.board.direction import Direction
from mine_game.domain.player import Player
from mine_game.application.game_status import GameStatus


class GameOverview:
    def __init__(self, player: Player, game_status):
        self.player_position = (player.x, player.y)
        self.mines_detonated = player.mines_detonated
        self.game_status = game_status


class MineGame:
    def __init__(self, board: Board):
        self.__board = board
        self.__mine_limit = 3
        self.__status = GameStatus.Active

    def get_overview(self) -> GameOverview:
        return GameOverview(self.__board.get_player(), self.__status)

    def move(self, direction: Direction):
        if self.__status == GameStatus.Active:
            self.__board.move_player(direction)
            self.__calculate_status()

    def __calculate_status(self):
        if self.__board.get_player().mines_detonated == self.__mine_limit:
            self.__status = GameStatus.Lost
        elif self.__board.get_player().y == self.__board.get_length_of_board() - 1:
            self.__status = GameStatus.Won
