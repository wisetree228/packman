from logic.field import Field
from objects.images.cells import Cell

class FieldDrawer:
    def __init__(self, field: Field):
        self.field_scheme = field.l

    def draw(self):
        for i in range(len(self.field_scheme)):
            print(self.field_scheme[i])
            for j in range(len(self.field_scheme[i])):
                cell = Cell(x = j*80, y = i*80, type = int(self.field_scheme[i][j]))
                cell.draw()