from Cell import Cell
from Position import Position, Direction


class Player:
    def __init__(self, startPos: Position = Position(), cell: Cell = Cell(Position())):
        self.position = startPos
        self.prevPosition = startPos
        self.cell = cell

    def playerCanMove(self, direction: Direction):
        wallsCurentPos = self.cell.walls
        return not wallsCurentPos[direction]

    def move(self, direction: Direction):
        if(not self.playerCanMove(direction)):
            print(f"Je kan daar niet naartoe!\nMuuren van [{self.position}] {self.cell.walls}")
            return
        self.prevPosition = Position(self.position.x, self.position.y)
        match direction:
            case Direction.Up:
                self.position.y += 1
            case Direction.Down:
                self.position.y -= 1
            case Direction.Left:
                self.position.x -= 1
            case Direction.Right:
                self.position.x += 1
