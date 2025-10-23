from Field import Field
from Player import Player
from Position import Direction

field = Field(5, 5, Player())
pl = field.player
print(field)
# field.getCell(Position(3,1)).walls = {Direction.Up: False, Direction.Right: False, Direction.Down: False, Direction.Left: False}
field.generateMaze()
print(field)

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
    field.update()
    print(f"pos     [{pl.position}]\nprevPos [{pl.prevPosition}]")
    print(f"current cell: {pl.cell}")
    print(field)
