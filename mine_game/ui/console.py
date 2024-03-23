from mine_game.application.mine_game import MineGame
from mine_game.domain.board.board import Board
from mine_game.domain.player import Player
from mine_game.domain.board.mine_generator import MineGenerator
from mine_game.domain.board.direction import Direction
import random


def run():
    board_dimensions = (8, 8)
    mine_game = MineGame(
        Board(Player((0, 0)), board_dimensions, MineGenerator(random, board_dimensions))
    )
    allowable_input = ["u", "l", "r", "d"]
    game_overview = mine_game.get_overview()

    while True:
        if game_overview.game_status != "InPlay":
            break
        user_input = input("Enter U,L,R,D\n").lower()
        if user_input[0] in allowable_input:
            mine_game.move(convert_to_direction(user_input[0]))
            game_overview = mine_game.get_overview()
            print(
                f"Player position: {game_overview.player_position}\nMines hit: {game_overview.mines_detonated}\nGame status: {game_overview.game_status}\n"
            )


def convert_to_direction(input: str) -> Direction:
    match input:
        case "u":
            return Direction.up
        case "d":
            return Direction.down
        case "l":
            return Direction.left
        case "r":
            return Direction.right
