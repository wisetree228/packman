from logic.field import Field
from objects.images.cells import Cell
from objects.images.seeds import Seed, Energizer
from objects.images.pacman import Pacman
from random import randint

class FieldDrawer:
    def __init__(self, field: Field):
        self.field_scheme = field.l
        self.cells = []
        self.seeds = []
        self.energ = []
        for i in range(len(self.field_scheme)):
            for j in range(len(self.field_scheme[i])):
                rand = randint(1, 40)
                cell = Cell(x = j*40, y = i*40, type = int(self.field_scheme[i][j]))
                self.cells.append(cell)
                if cell.type == 0 and i<16:
                    if rand != 19:
                        seed = Seed(x = j*40+20, y = i*40+20)
                        self.seeds.append(seed)
                    else:
                        energ = Energizer(x = j*40+20, y = i*40+20)
                        self.energ.append(energ)

    def draw(self):
        for i in self.cells:
            i.draw()
        for i in self.seeds:
            i.draw()
        for i in self.energ:
            i.draw()

    def eat(self, pacman: Pacman):
        for seed in self.seeds:
            if seed.x in range(pacman.x, pacman.x+40) and seed.y in range(pacman.y, pacman.y+40):
                self.seeds.remove(seed)
        for en in self.energ:
            if en.x in range(pacman.x, pacman.x+40) and en.y in range(pacman.y, pacman.y+40):
                self.energ.remove(en)