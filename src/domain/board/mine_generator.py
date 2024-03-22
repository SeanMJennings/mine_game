import random
from src.domain.mine import Mine


class MineGenerator:

    def __init__(self, random_generator: random, board_dimensions: tuple[int, int]):
        self.__random_generator = random_generator
        self.__board_dimensions = board_dimensions

    def generate_mines(self):
        mines = []
        for x in range(self.__board_dimensions[0]):
            for y in range(self.__board_dimensions[1]):
                if self.__random_generator.random() != 1.0 or (x == 0 and y == 0):
                    continue
                mines.append(Mine((x, y)))
        return mines
