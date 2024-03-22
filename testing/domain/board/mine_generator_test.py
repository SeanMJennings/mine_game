from testing.specification import *
from testing.domain.board.mine_generator_steps import *


def test_generates_a_board_with_undetonated_mines():
    Given(a_mine_generator)
    When(generating_mines)
    Then(the_board_is_filled_with_undetonated_mines)
    And(the_bottom_left_tile_is_empty)


def test_mines_do_not_share_position():
    Given(a_mine_generator)
    When(generating_mines)
    Then(no_mines_share_position)
