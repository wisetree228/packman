from objects.base import BaseObject
import pyray
class Cell(BaseObject):
    def __init__(self, x, y, type=0):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        if self.type == 0:
            color = pyray.BLACK
        elif self.type == 1:
            color = pyray.PURPLE
        elif self.type == 2:
            color = pyray.BLUE
        else:
            color = pyray.GREEN
        pyray.draw_rectangle(self.x, self.y, 60, 60, color)
