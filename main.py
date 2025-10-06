class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

class Field:
    def __init__(self, sizeX = 5, sizeY = 5):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.field = self.generateField(sizeX, sizeY)

    def generateField(self, sizeX: int, sizeY: int):
        field = []
        for y in range(sizeY):
            field.append([])
            for x in range(sizeX):
                field[y].append(0)
        return field

    def __str__(self):
        string = ""
        for y in self.field:
            for x in y:
                string += f"{x} "
            string += "\n"
        return string

field = Field()
print(field)
