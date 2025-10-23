from enum import Enum


class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4


class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x:{self.x}, y:{self.y}"
