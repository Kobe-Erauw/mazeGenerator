from Field import Field
from Player import Player
from Position import Direction

sizeY = int(input("Height     (#characters): "))
sizeX = int(input("Width      (#characters): "))
duration = float(input("Animation duration (sec): "))
field = Field(sizeX, sizeY, Player())
pl = field.player
# field.getCell(Position(3,1)).walls = {Direction.Up: False, Direction.Right: False, Direction.Down: False, Direction.Left: False}
field.generateMaze(duration)
field.update()
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
    print(field)
