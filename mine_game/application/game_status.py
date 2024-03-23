from enum import Enum


class GameStatus(Enum):
    Lost = "Lost",
    Active = "Active",
    Won = "Won"

    def __str__(self):
        return self.value[0] if len(self.value) == 1 else self.value
