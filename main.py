from Field import Field
from Player import Player
from Position import Direction

sizeX = input("height     (#characters): ")
sizeY = input("width      (#characters): ")
duration =  input("animation duration (sec): ")
field = Field(60, 30, Player())
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
