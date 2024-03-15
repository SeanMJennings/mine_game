import pytest
from testing.specification import *
from testing.domain.board.board_steps import *

@pytest.mark.parametrize("movement,position", [("Up", (1,2)),("Down", (1,0)),("Left", (0,1)),("Right", (2,1))])
def test_move_player(movement,position):
    Given(a_player_in_position((1,1)))
    And(a_board_of_size((4,4)))
    When(moving_a_player(movement))
    Then(a_player_moves_to(position))

@pytest.mark.parametrize("movement,position", [("Up", (4,4)),("Down", (0,0)),("Left", (0,0)),("Right", (4,4))])
def test_does_not_let_player_move_off_board(movement,position):
    Given(a_player_in_position(position))
    And(a_board_of_size((4,4)))
    When(moving_a_player(movement))
    Then(a_player_moves_to(position))
    
def test_lets_player_detonate_mine():
    Given(a_player_in_position((0,0)))
    And(a_board_full_of_mines_with_size((4,4)))
    When(moving_a_player("up"))
    Then(a_player_detonates_a_mine)