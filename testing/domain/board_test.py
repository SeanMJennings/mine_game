import pytest
from src.domain.board import Board

def test_move_player_up():
    board = Board()
    board.move_player('Up')
    position = board.get_player()
    assert position.x == 0
    assert position.y == 1
    
def test_move_player_down():
    board = Board()
    board.move_player('Up')
    board.move_player('Down')
    position = board.get_player()
    assert position.x == 0
    assert position.y == 0

if __name__ == "__main__":
    pytest.main(["board_test.py", "-s"])