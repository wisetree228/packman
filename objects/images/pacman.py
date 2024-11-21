import pyray
from raylib import colors
from objects.base import BaseObject
from logic.field import Field
import math
Field_structure = Field().l

class Pacman(BaseObject):
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 80  # Ширина пакмана
        self.height = 80  # Высота пакмана
        self.direction = "RIGHT"  # Начальное направление
        self.cellx = 0
        self.celly = 0

    def update(self):
        self.cellx = self.x//80
        self.celly = self.y // 80
        print(Field_structure[self.celly][self.cellx])
        # Обновление положения пакмана в зависимости от направления
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            if int(Field_structure[self.celly][self.cellx-1]) == 1:
                if self.x==(self.cellx-1)*80+80:
                    self.x = self.x
                else:
                    self.x -= self.speed
            else:
                self.x -= self.speed
        elif self.direction == "RIGHT":
            if int(Field_structure[self.celly][self.cellx+1]) == 1:
                self.x = self.cellx*80
            else:
                self.x += self.speed
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > pyray.get_screen_width():
            self.x = pyray.get_screen_width() - self.width
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > pyray.get_screen_height():
            self.y = pyray.get_screen_height() - self.height


    def draw(self):
        # Рисуем пакмана (жёлтый прямоугольник)
        pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.YELLOW)
    def game(self):
        if pyray.is_key_down(pyray.KEY_W):
            self.set_direction("UP")
        elif pyray.is_key_down(pyray.KEY_S):
            self.set_direction("DOWN")
        elif pyray.is_key_down(pyray.KEY_A):
            self.set_direction("LEFT")
        elif pyray.is_key_down(pyray.KEY_D):
            self.set_direction("RIGHT")
        self.update()
    def set_direction(self, direction):
        # Задание направления движения пакмана
        self.direction = direction