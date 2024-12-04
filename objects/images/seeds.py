from objects.base import BaseObject
import pyray
from raylib import colors
class Seed(BaseObject):
    def __init__(self, x, y):
        self.weight = 10
        self.x = x
        self.y = y

    def draw(self):
        pyray.draw_circle(self.x, self.y, 3, colors.YELLOW)


class Energizer(BaseObject):
    def __init__(self, x, y):
        self.weight = 50
        self.x = x
        self.y = y

    def draw(self):
        pyray.draw_circle(self.x, self.y, 8, colors.YELLOW)