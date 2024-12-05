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
        pyray.draw_circle(self.x - self.size // 2,self.y - self.size // 4, self.size // 2, pyray.RED)
        pyray.draw_circle(self.x + self.size // 2, self.y - self.size // 4, self.size // 2, pyray.RED)
        #pyray.draw_triangle((self.x - self.size // 2, self.y - self.size // 4),(self.x + self.size // 2, self.y - self.size // 4), (self.x, self.y + self.size // 2), pyray.RED)
        pyray.draw_circle(self.x, self.y + self.size // 4, self.size//1.7, pyray.RED)
        pyray.draw_text(str(self.count_hp), self.x-10, self.y-10, 40, pyray.WHITE)
