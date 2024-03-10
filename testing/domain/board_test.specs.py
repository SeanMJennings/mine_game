import pytest
from specification import *
from board_steps import *

@pytest.mark.parametrize("movement,position", [("Up", (1,2)),("Down", (1,0)),("Left", (0,1)),("Right", (2,1))])
def test_move_player(movement,position):
    Given(a_board)
    When(moving_a_player(movement))
    Then(a_player_moves(position))