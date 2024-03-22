from random import Random
from pytest_mock import MockerFixture
from src.domain.board.mine_generator import MineGenerator

mine_generator = None
board_dimensions = None
random_generator = None
mines = None


def a_mine_generator(*args):
    global mine_generator, board_dimensions
    board_dimensions = (5, 5)

    def always_one():
        return 1.0

    mock = MockerFixture(None)
    random_generator = mock.patch.object(
        Random, "random", type("", (object,), {"random": always_one})
    )
    mine_generator = MineGenerator(random_generator, board_dimensions)


def generating_mines(*args):
    global mine_generator, mines
    mines = mine_generator.generate_mines()


def no_mines_share_position(*args):
    global mines
    mine_set = set(mines)
    assert len(mine_set) == (board_dimensions[0] * board_dimensions[1]) - 1


def the_board_is_filled_with_undetonated_mines(*args):
    global mines, board_dimensions
    assert len(mines) == (board_dimensions[0] * board_dimensions[1]) - 1
    index = 0
    for x in range(board_dimensions[0]):
        for y in range(board_dimensions[1]):
            if x == 0 and y == 0:
                continue
            mine = mines[index]
            assert mine.position == (x, y)
            assert mine.detonated == False
            index = index + 1


def the_bottom_left_tile_is_empty(*args):
    return
