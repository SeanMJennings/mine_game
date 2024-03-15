from testing.specification import *
from testing.domain.board.mine_generator_steps import *

def test_produces_a_board_filled_with_mines():
    Given(a_mine_generator)
    When(generating_mines)
    Then(the_board_is_filled_with_mines)