import pyray
from raylib import colors
from objects.base import BaseObject
from logic.field import Field
import math

class  Life(BaseObject):
    def __init__(self, x, y, size=10, count_hp=3):
        self.x = x
        self.y = y
        self.size = size
        self.count_hp = count_hp
    def draw(self):
        # Вверхняя часть сердечка
        c = 0
        for i in range(self.count_hp):
            pyray.draw_circle(self.x+c, self.y, 20, pyray.RED)
            c+=40

