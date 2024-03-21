from random import Random
from pytest_mock import MockerFixture
from src.domain.board.mine_generator import MineGenerator

class FakeMineGenerator():
    def __init__(self, generate_mines: bool, board_dimensions: tuple[int,int]):
        self.__generate_mines = generate_mines
        self.__board_dimensions = board_dimensions
        def always_one():
            return 1.0
        def always_zero():
            return 0
        mock = MockerFixture(None)
        if (self.__generate_mines):
            self.__random_generator = mock.patch.object(Random, 'random', type('', (object,), {'random': always_one}))
        else:
            self.__random_generator = mock.patch.object(Random, 'random', type('', (object,), {'random': always_zero}))
        self.__mine_generator = MineGenerator(self.__random_generator, self.__board_dimensions)
    def generate_mines(self):
        return self.__mine_generator.generate_mines()