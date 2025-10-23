from Position import Position, Direction


class Cell:
    def __init__(self, position: Position, value: str = "0"):
        self.walls = {
                Direction.Up: True,
                Direction.Right: True,
                Direction.Down: True,
                Direction.Left: True
            }
        self.position = position
        self.value = value
        self.isVisited = False

    def __str__(self):
        return f"Cell[{str(self.position)}] {self.walls}"
