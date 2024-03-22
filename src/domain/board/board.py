from src.domain.board.direction import Direction
from src.domain.player import Player
from src.domain.board.mine_generator import MineGenerator


class Board:

    def __init__(
        self, player: Player, dimensions: tuple[int, int], mine_generator: MineGenerator
    ):
        self.__player = player
        self.__dimensions = dimensions
        self.__mines = mine_generator.generate_mines()

    def move_player(self, direction: Direction):
        direction = Direction[direction.lower()]
        match direction:
            case Direction.up:
                if self.__inside_top_of_board():
                    self.__player.move(direction)
            case Direction.down:
                if self.__inside_bottom_of_board():
                    self.__player.move(direction)
            case Direction.left:
                if self.__inside_left_of_board():
                    self.__player.move(direction)
            case Direction.right:
                if self.__inside_right_of_board():
                    self.__player.move(direction)
        self.__check_for_mine()

    def __inside_right_of_board(self):
        return self.__player.x + 1 <= self.__dimensions[0] - 1

    def __inside_left_of_board(self):
        return self.__player.x - 1 >= 0

    def __inside_bottom_of_board(self):
        return self.__player.y - 1 >= 0

    def __inside_top_of_board(self):
        return self.__player.y + 1 <= self.__dimensions[1] - 1

    def __check_for_mine(self):
        mines = list(
            filter(
                lambda mine: mine.position[0] == self.__player.x
                and mine.position[1] == self.__player.y
                and mine.detonated is False,
                self.__mines,
            )
        )
        if len(mines) == 1:
            mines[0].detonate()
            self.__player.mine_hit()

    def get_player(self):
        return self.__player

    def get_length_of_board(self):
        return self.__dimensions[1]
