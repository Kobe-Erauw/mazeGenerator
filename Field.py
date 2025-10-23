from random import shuffle

from Cell import Cell
from Player import Player
from Position import Position, Direction


class Field:
    def __init__(self, sizeX: int = 5, sizeY: int = 5, player: Player = Player(), startPosition: Position = Position()):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.field = self.generateBlankField(sizeX, sizeY)
        self.player = Player(startPosition, self.getCell(startPosition))
        self.startPosition = startPosition
        self.itaration = 0

    def generateBlankField(self, sizeX: int, sizeY: int):
        field = []
        for y in range(sizeY):
            field.append([])
            for x in range(sizeX):
                field[y].append(Cell(Position(x, y)))
        return field

    def generateMaze(self):
        self.makeWay(self.getCell(self.startPosition))

    def makeWay(self, cell: Cell):
        print(self.__str__())
        cell.isVisited = True
        unvisited = self.getUnvisitedNeighbours(cell)
        unvisitedKeys = list(unvisited.keys())
        shuffle(unvisitedKeys)
        for key in unvisitedKeys:
            cell.walls[key] = False
            unvisited[key].walls[self.getOppositDirection(key)] = False
            self.makeWay(unvisited[key])

    def getUnvisitedNeighbours(self, cell: Cell):
        unvisited = {}
        neighbours = self.getNeiggbours(cell)
        for dir, neig in neighbours.items():
            if(not neig): continue
            if(not neig.isVisited):
                unvisited[dir] = neig
        return unvisited

    def isValidPosition(self, position: Position):
        return not (position.x < 0 or position.x >= self.sizeX or position.y < 0 or position.y >= self.sizeY)


    def getNeiggbours(self, cell: Cell):
        neighbours = {}
        position = cell.position
        neighbours[Direction.Up] = self.getCellOrNone(Position(position.x, position.y + 1))
        neighbours[Direction.Down] = self.getCellOrNone(Position(position.x, position.y - 1))
        neighbours[Direction.Right] = self.getCellOrNone(Position(position.x + 1, position.y))
        neighbours[Direction.Left] = self.getCellOrNone(Position(position.x - 1, position.y))
        return neighbours

    def setPlayerPosition(self):
        self.setValue(self.player.prevPosition, "0")
        self.setValue(self.player.position, "X")
        self.player.cell = self.getCell(self.player.position)

    def setValue(self, position: Position, value: str):
        # if(not self.isValidPosition(position)):
        #     print(f"Het is Ilegaal om [{position}] te betreden")
        #     self.player.position = self.player.prevPosition
        #     position = self.player.position
        self.field[self.sizeY - position.y - 1][position.x].value = value

    def getCell(self, position: Position) -> Cell:
        return self.field[position.y][position.x]

    def getCellOrNone(self, position: Position):
        if(self.isValidPosition(position)):
            return self.getCell(position)
        return None

    def update(self):
        self.setPlayerPosition()

    def getOppositDirection(self, direction: Direction):
        match direction:
            case Direction.Up:
                return Direction.Down
            case Direction.Right:
                return Direction.Left
            case Direction.Down:
                return Direction.Up
            case Direction.Left:
                return Direction.Right
        return None

    def __str__(self):
        string = ""
        for y in self.field:
            underline = ""
            for cell in y:
                if(cell.walls[Direction.Down]):
                    underline += "― "
                else:
                    underline += "  "
                if(cell.walls[Direction.Right]):
                    string += f"{cell.value}|"
                else:
                    string += f"{cell.value} "
            string += "\n" + underline + "\n"
        return string
