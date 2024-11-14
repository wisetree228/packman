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
        elif self.type == 2: #ghost room
            color = pyray.BLUE
        else: #teleport
            color = pyray.GREEN
        pyray.draw_rectangle(self.x, self.y, 80, 80, color)
