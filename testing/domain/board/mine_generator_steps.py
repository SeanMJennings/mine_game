import pytest
import random
from pytest_mock import MockerFixture
from src.domain.board.mine_generator import MineGenerator

mine_generator = None
board_dimensions = None
random_generator = None
mines = None

def a_mine_generator(*args):
    global board_dimensions, mine_generator
    board_dimensions = (5,5)
    def _random():
        return 1
    fake_random_generator = type('', (object,), {'random': _random})
    mock = MockerFixture(None)
    random_generator = mock.patch.object(random, 'random', fake_random_generator)
    mine_generator = MineGenerator(random_generator, board_dimensions)
    
def generating_mines(*args):
    global mine_generator, mines
    mines = mine_generator.generate_mines()
    
def the_board_is_filled_with_mines(*args):
    global mines, board_dimensions
    assert len(mines) == board_dimensions[0] * board_dimensions[1]
    index = 0
    for x in range(board_dimensions[0]):
        for y in range(board_dimensions[1]):
            mine = mines[index]
            assert mine.position == (x,y)
            assert mine.detonated == False
            index = index + 1

    