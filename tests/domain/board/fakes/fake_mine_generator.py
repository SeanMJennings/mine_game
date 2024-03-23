from random import Random
import math
from pytest_mock import MockerFixture
from mine_game.domain.board.mine_generator import MineGenerator


class FakeMineGenerator:
    def __init__(self, generate_mines: bool, board_dimensions: tuple[int, int]):
        self.__generate_mines = generate_mines
        self.__board_dimensions = board_dimensions
        self.__seed = math.floor(self.__board_dimensions[0] * self.__board_dimensions[1] / self.__board_dimensions[0])

        def always_max(*args):
            return self.__seed

        def always_zero(*args):
            return 0

        mock = MockerFixture(None)
        if self.__generate_mines:
            self.__random_generator = mock.patch.object(
                Random, "random", type("", (object,), {"randint": always_max})
            )
        else:
            self.__random_generator = mock.patch.object(
                Random, "random", type("", (object,), {"randint": always_zero})
            )
        self.__mine_generator = MineGenerator(
            self.__random_generator, self.__board_dimensions
        )

    def generate_mines(self):
        return self.__mine_generator.generate_mines()
