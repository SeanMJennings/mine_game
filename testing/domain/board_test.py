import pytest
from src.domain.board import Board

def test_move_player_up():
    board = Board()
    board.move_player('Up')
    position = board.get_player()
    assert position.x == 0
    assert position.y == 1