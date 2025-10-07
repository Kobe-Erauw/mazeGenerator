from enum import Enum

class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4
    def __str__(self):
        return "test"

class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x:{self.x}, y:{self.y}"

class Cell:
    def __init__(self, position: Position, 
                 value: str = "0", 
                 walls: dict = {
                 Direction.Up: False, Direction.Right: False, Direction.Down: False, Direction.Left: False
                 }):
        self.walls = walls
        self.postition = position
        self.value = value

    def __str__(self):
        return str(self.walls)

class Player:
    def __init__(self, startPos: Position = Position(), cell: Cell = Cell(Position())):
        self.position = startPos
        self.cell = cell

    def playerCanMove(self, direction: Direction):
        wallsCurentPos = self.cell.walls
        return not wallsCurentPos[direction]

    def move(self, direction: Direction):
        if(not self.playerCanMove(direction)):
            print(f"Je kan daar niet naartoe!\nMuuren van [{self.position}] {self.cell}")
            return
        self.prevPosition = Position(self.position.x,self.position.y)
        match direction:
            case Direction.Up:
                self.position.y += 1
            case Direction.Down:
                self.position.y -= 1
            case Direction.Left:
                self.position.x -= 1
            case Direction.Right:
                self.position.x += 1

class Field:
    def __init__(self, sizeX: int = 5, sizeY: int = 5, player: Player = Player(), startPosition: Position = Position()):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.field = self.generateBlankField(sizeX, sizeY)
        self.player = Player(startPosition, self.getCell(startPosition))

    def generateBlankField(self, sizeX: int, sizeY: int):
        field = []
        for y in range(sizeY):
            field.append([])
            for x in range(sizeX):
                field[y].append(Cell(Position(x,y)))
        return field

    def setPlayerPosition(self):
        self.field = self.generateBlankField(self.sizeX,self.sizeY)
        self.setValue(self.player.position, "X")
        self.player.cell = self.getCell(self.player.position)

    def setValue(self, position: Position, value: str):
        if(position.x < 0 or position.x >= self.sizeX or position.y < 0 or position.y >= self.sizeY):
            print(f"Het is Ilegaal om [{position}] te betreden")
            self.player.position = self.player.prevPosition
            position = self.player.position
        self.field[self.sizeY - position.y - 1][position.x].value = value

    def getCell(self, position: Position):
        return self.field[position.y][position.x]

    def update(self):
        self.setPlayerPosition()

    def __str__(self):
        string = ""
        for y in self.field:
            for cell in y:
                string += f"{cell.value} "
            string += "\n"
        return string

field = Field(player=Player())
pl = field.player

while True:
    match input("Direction: "):
        case "z":
            pl.move(Direction.Up)
        case "s":
            pl.move(Direction.Down)
        case "d":
            pl.move(Direction.Right)
        case "q":
            pl.move(Direction.Left)
    print(f"pos     [{pl.position}]\nprevPos [{pl.prevPosition}]")
    field.update()
    print(field)
