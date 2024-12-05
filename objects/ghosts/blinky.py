import pyray
from raylib import colors
from objects.base import BaseObject
from logic.field import Field
import math
import time
import random
Field_structure = Field().l
class BlinkyGhost(BaseObject):

    def __init__(self, x, y, speed, width=40, height=40, direction="RIGHT", past_derection = ""):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.direction = direction
        self.past_derection = past_derection


    def draw(self):
        pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.RED)

    def update(self):
        self.cellx = self.x // 40
        self.celly = self.y // 40
        # print(Field_structure[self.celly][self.cellx], self.y, self.celly)
        # Обновление положения пакмана в зависимости от направления
        if self.direction == "UP":
            if int(Field_structure[self.celly - 1][self.cellx]) == 1 or (
                    int(Field_structure[self.celly - 1][self.cellx + 1]) == 1 and self.x != (self.cellx + 1) * 40 - 40):
                if self.y == (self.celly - 1) * 40 + 40:
                    self.y = self.y
                else:
                    self.y -= self.speed

            else:
                self.y -= self.speed
        elif self.direction == "DOWN":
            if int(Field_structure[self.celly + 1][self.cellx]) == 1 or (
                    int(Field_structure[self.celly + 1][self.cellx + 1]) == 1 and self.x != (self.cellx + 1) * 40 - 40):
                # if self.y == (self.celly+1) * 80+80:
                self.y = self.y
                # else:
                # self.y += self.speed

            else:
                self.y += self.speed
        elif self.direction == "LEFT":
            if int(Field_structure[self.celly][self.cellx - 1]) == 1 or (
                    int(Field_structure[self.celly + 1][self.cellx - 1]) == 1 and self.y != (self.celly + 1) * 40 - 40):
                if self.x == (self.cellx - 1) * 40 + 40:
                    self.x = self.x
                else:
                    self.x -= self.speed
            else:
                self.x -= self.speed
        elif self.direction == "RIGHT":
            if int(Field_structure[self.celly][self.cellx + 1]) == 1 or (
                    int(Field_structure[self.celly + 1][self.cellx + 1]) == 1 and self.y != (self.celly + 1) * 40 - 40):
                self.x = self.cellx * 40
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


    def game(self):
        self.cellx = self.x // 40
        self.celly = self.y // 40
        if self.x==480 and self.y==280:
            self.x=560
        l = []
        l.append(self.direction)
        if (int(Field_structure[self.celly - 1][self.cellx]) == 0 and (int(Field_structure[self.celly - 1][self.cellx + 1]) != 1 or self.x == (self.cellx + 1) * 40 - 40)) and (self.direction!="DOWN" or (int(Field_structure[self.celly + 1][self.cellx]) == 1 and int(Field_structure[self.celly][self.cellx-1]) == 1 and int(Field_structure[self.celly][self.cellx+1]) == 1)):

            #if int(Field_structure[self.celly - 1][self.cellx]) != 1:
            l.append("UP")
        if (int(Field_structure[self.celly + 1][self.cellx]) == 0 and (int(Field_structure[self.celly + 1][self.cellx + 1]) != 1 or self.x == (self.cellx + 1) * 40 - 40)) and (self.direction!="UP" or (int(Field_structure[self.celly - 1][self.cellx]) == 1 and int(Field_structure[self.celly][self.cellx-1]) == 1 and int(Field_structure[self.celly][self.cellx+1]) == 1)):
            #if int(Field_structure[self.celly + 1][self.cellx]) != 1:
            l.append("DOWN")
        if (int(Field_structure[self.celly][self.cellx - 1]) == 0 and (int(Field_structure[self.celly + 1][self.cellx - 1]) != 1 or self.y == (self.celly + 1) * 40 - 40)) and (self.direction!="RIGHT" or (int(Field_structure[self.celly][self.cellx+1]) == 1 and int(Field_structure[self.celly - 1][self.cellx]) == 1 and int(Field_structure[self.celly+1][self.cellx]) == 1)):
            #if int(Field_structure[self.celly][self.cellx - 1]) != 1:

            l.append("LEFT")
        if (int(Field_structure[self.celly][self.cellx + 1]) == 0 and (int(Field_structure[self.celly + 1][self.cellx + 1]) != 1 or self.y == (self.celly + 1) * 40 - 40)) and (self.direction!="LEFT" or (int(Field_structure[self.celly][self.cellx-1]) == 1 and int(Field_structure[self.celly - 1][self.cellx]) == 1 and int(Field_structure[self.celly+1][self.cellx]) == 1)):
            #if int(Field_structure[self.celly][self.cellx + 1]) != 1:
            l.append("RIGHT")
        random_direction=random.choice(l)
        self.set_direction(random_direction)
        self.update()
    def set_direction(self, direction):
        # Задание направления движения пакмана
        self.past_derection = self.past_derection
        self.direction = direction
