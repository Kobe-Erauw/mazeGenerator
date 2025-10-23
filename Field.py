from random import shuffle
from time import sleep
from rich.console import Console
from rich.live import Live

from Cell import Cell
from Player import Player
from Position import Position, Direction


class Field:
    def __init__(self, sizeX: int = 5, sizeY: int = 5, player: Player = Player(), startPosition: Position = Position()):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.destination = Position(sizeX - 1, sizeY - 1)
        self.field = self.generateBlankField(sizeX, sizeY)
        self.player = Player(startPosition, self.getCell(startPosition))
        self.startPosition = startPosition
        self.console = Console()

    def generateBlankField(self, sizeX: int, sizeY: int):
        field = []
        for y in range(sizeY):
            field.append([])
            for x in range(sizeX):
                field[y].append(Cell(Position(x, y)))
        return field

    def generateMaze(self, animDuration: float):
        with Live(self.__str__(), console=self.console, refresh_per_second=10) as live:
            self.makeWay(self.getCell(self.startPosition), live, animDuration)
            live.update("")
        self.setValue(self.destination, "#")

    def makeWay(self, cell: Cell, live: Live, animDuration: float):
        cell.isVisited = True
        live.update(self.__str__())
        sleep(animDuration / (self.sizeX * self.sizeY))
        unvisited = self.getUnvisitedNeighbours(cell)
        unvisitedKeys = list(unvisited.keys())
        shuffle(unvisitedKeys)
        for key in unvisitedKeys:
            if not unvisited[key].isVisited:
                cell.walls[key] = False
                unvisited[key].walls[self.getOppositDirection(key)] = False
                self.makeWay(unvisited[key], live, animDuration)

    def getUnvisitedNeighbours(self, cell: Cell):
        unvisited = {}
        neighbours = self.getNeiggbours(cell)
        for dir, neig in neighbours.items():
            if not neig: continue
            if not neig.isVisited:
                unvisited[dir] = neig
        return unvisited

    def isValidPosition(self, position: Position):
        return not (position.x < 0 or position.x >= self.sizeX or position.y < 0 or position.y >= self.sizeY)

    def getNeiggbours(self, cell: Cell):
        neighbours = {}
        position = cell.position
        neighbours[Direction.Up] = self.getCellOrNone(Position(position.x, position.y - 1))
        neighbours[Direction.Down] = self.getCellOrNone(Position(position.x, position.y + 1))
        neighbours[Direction.Right] = self.getCellOrNone(Position(position.x + 1, position.y))
        neighbours[Direction.Left] = self.getCellOrNone(Position(position.x - 1, position.y))
        return neighbours

    def setPlayerPosition(self):
        self.setValue(self.player.prevPosition, " ")
        self.setValue(self.player.position, "X")
        self.player.cell = self.getCell(self.player.position)

    def setValue(self, position: Position, value: str):
        self.getCell(position).value = value

    def getCell(self, position: Position) -> Cell:
        return self.field[position.y][position.x]

    def getCellOrNone(self, position: Position):
        if self.isValidPosition(position):
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
        string = " "
        for row in range(self.sizeX):
            string += "― "
        string += "\n"
        for y in range(self.sizeY):
            string += "|"
            underline = " "
            for x in range(self.sizeX):
                cell = self.getCell(Position(x, y))
                if cell.walls[Direction.Down]:
                    underline += "― "
                else:
                    underline += "  "
                if cell.walls[Direction.Right]:
                    string += f"{cell.value}|"
                else:
                    string += f"{cell.value} "
            string += "\n" + underline + "\n"
        return string
