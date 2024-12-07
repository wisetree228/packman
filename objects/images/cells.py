from objects.base import BaseObject
import pyray
class Cell(BaseObject):
    def __init__(self, x, y, type=0):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        if self.type == 0: #void
            color = pyray.BLACK
        elif self.type == 1: #wall
            color = pyray.PURPLE
        elif self.type == 2: #tp
            color = pyray.BLUE
        else: #void without cell
            color = pyray.BLACK
        pyray.draw_rectangle(self.x, self.y, 80, 80, color)
