import pytest
from testing.specification import *
from testing.application.mine_game_steps import *

def test_returns_game_overview():
    Given(a_game_with_no_mines)
    When(requesting_game_overview)
    Then(the_overview_is_returned)
    
def test_lets_player_lose():
    Given(a_game_with_mines)
    When(moving_up_three_spaces)
    Then(the_game_is_lost)
    
def test_lets_player_win():
    Given(a_game_with_no_mines)
    When(moving_to_top_of_board)
    Then(the_game_is_won)
    
def test_does_not_allow_movement_if_lost():
    Given(game_is_lost)
    When(trying_to_move_player_down)
    Then(dead_player_does_not_move)
    
def test_does_not_allow_movement_if_game_is_won():
    Given(game_is_won)
    When(trying_to_move_player_down)
    Then(alive_player_does_not_move)