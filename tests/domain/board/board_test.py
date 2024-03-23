import pytest
from mine_game.domain.board.direction import Direction
from tests.specification import *
from tests.domain.board.board_steps import *


@pytest.mark.parametrize(
    "movement,position",
    [(Direction.up, (1, 2)), (Direction.down, (1, 0)), (Direction.left, (0, 1)), (Direction.right, (2, 1))],
)
def test_move_player(movement, position):
    Given(a_player_in_position((1, 1)))
    And(a_board_of_size((4, 4)))
    When(moving_a_player(movement))
    Then(a_player_moves_to(position))


@pytest.mark.parametrize(
    "movement,position",
    [(Direction.up, (4, 4)), (Direction.down, (0, 0)), (Direction.left, (0, 0)), (Direction.right, (4, 4))],
)
def test_does_not_let_player_move_off_board(movement, position):
    Given(a_player_in_position(position))
    And(a_board_of_size((4, 4)))
    When(moving_a_player(movement))
    Then(a_player_moves_to(position))


def test_lets_player_detonate_mine():
    Given(a_player_in_position((0, 0)))
    And(a_board_full_of_mines_with_size((4, 4)))
    When(moving_a_player(Direction.up))
    Then(a_player_detonates_a_mine)


def test_does_not_detonate_mine_twice():
    Given(a_player_in_position((0, 0)))
    And(a_board_full_of_mines_with_size((4, 4)))
    When(moving_a_player(Direction.up))
    And(moving_a_player(Direction.down))
    And(moving_a_player(Direction.up))
    Then(the_mine_only_detonates_once)
