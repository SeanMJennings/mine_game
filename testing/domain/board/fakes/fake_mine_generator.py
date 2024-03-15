from random import Random
from pytest_mock import MockerFixture
from src.domain.board.mine_generator import MineGenerator

class FakeMineGenerator():
    def __init__(self, generate_mines: bool, board_dimensions: tuple[int,int]):
        self._generate_mines = generate_mines
        self._board_dimensions = board_dimensions
        def always_one():
            return 1.0
        def always_zero():
            return 0
        mock = MockerFixture(None)
        if (self._generate_mines):
            self._random_generator = mock.patch.object(Random, 'random', type('', (object,), {'random': always_one}))
        else:
            self._random_generator = mock.patch.object(Random, 'random', type('', (object,), {'random': always_zero}))
        self._random_generator.random()
        self._mine_generator = MineGenerator(self._random_generator, self._board_dimensions)
    def generate_mines(self):
        return self._mine_generator.generate_mines()