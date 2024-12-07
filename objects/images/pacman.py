import pyray
from raylib import colors
from objects.base import BaseObject
from logic.field import Field
import math
from objects.ghosts.blinky import BlinkyGhost
from objects.ghosts.pinky import PinkyGhost
from objects.ghosts.inky import InkyGhost
from objects.ghosts.clyde import ClydeGhost
from objects.score import ScoreDrawer
Field_structure = Field().l

class Pacman(BaseObject):
    def __init__(self, x, y, speed=4):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 40  # Ширина пакмана
        self.height = 40  # Высота пакмана
        self.direction = "RIGHT"  # Начальное направление
        self.cellx = 0
        self.celly = 0
        self.rage_timer = 0
        self.rage_mod = False

    def update(self, scoredrawer: ScoreDrawer):
        if self.rage_timer>0:
            self.rage_timer-=1
        if self.rage_timer == 0:
            self.rage_mod = False
            scoredrawer.eaten = 0
        self.cellx = self.x//40
        self.celly = self.y // 40
        #print(Field_structure[self.celly][self.cellx], self.y, self.celly)
        # Обновление положения пакмана в зависимости от направления
        if self.direction == "UP":
            if int(Field_structure[self.celly-1][self.cellx]) == 1 or (int(Field_structure[self.celly-1][self.cellx+1]) == 1 and self.x!=(self.cellx+1)*40-40):
                if self.y == (self.celly-1) * 40+40:
                    self.y = self.y
                else:
                    self.y -= self.speed

            else:
                self.y -= self.speed
        elif self.direction == "DOWN":
            if int(Field_structure[self.celly+1][self.cellx]) == 1 or (int(Field_structure[self.celly+1][self.cellx+1]) == 1 and self.x!=(self.cellx+1)*40-40):
                #if self.y == (self.celly+1) * 80+80:
                self.y = self.y
                #else:
                    #self.y += self.speed

            else:
                self.y += self.speed
        elif self.direction == "LEFT":
            if int(Field_structure[self.celly][self.cellx-1]) == 1 or (int(Field_structure[self.celly+1][self.cellx-1]) == 1 and self.y!=(self.celly+1)*40-40):
                if self.x==(self.cellx-1)*40+40:
                    self.x = self.x
                else:
                    self.x -= self.speed
            else:
                self.x -= self.speed
        elif self.direction == "RIGHT":
            if int(Field_structure[self.celly][self.cellx+1]) == 1 or (int(Field_structure[self.celly+1][self.cellx+1]) == 1 and self.y!=(self.celly+1)*40-40):
                self.x = self.cellx*40
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

    def ghost_collision(self, ClydeGhost, InkyGhost, PinkyGhost, BlinkyGhost, scoredrawer: ScoreDrawer):

        if ((0<=abs(self.x-ClydeGhost.x)<=40 and 0<=abs(self.y-ClydeGhost.y)<40) or (38<=abs(self.y-ClydeGhost.y)<=42) and 0<=abs(self.x-ClydeGhost.x)<=40):
            scoredrawer.update_score(scoredrawer.score+(scoredrawer.eaten*200))
            return 1
        if ((0<=abs(self.x-InkyGhost.x)<=40 and 0<=abs(self.y-InkyGhost.y)<40) or (38<=abs(self.y-InkyGhost.y)<=42) and 0<=abs(self.x-InkyGhost.x)<=40):
            scoredrawer.update_score(scoredrawer.score + (scoredrawer.eaten * 200))
            return 2
        if ((0<=abs(self.x-PinkyGhost.x)<=40 and 0<=abs(self.y-PinkyGhost.y)<40) or (38<=abs(self.y-PinkyGhost.y)<=42) and 0<=abs(self.x-PinkyGhost.x)<=40):
            scoredrawer.update_score(scoredrawer.score + (scoredrawer.eaten * 200))
            return 3
        if ((0<=abs(self.x-BlinkyGhost.x)<=40 and 0<=abs(self.y-BlinkyGhost.y)<40) or (38<=abs(self.y-BlinkyGhost.y)<=42) and 0<=abs(self.x-BlinkyGhost.x)<=40):
            scoredrawer.update_score(scoredrawer.score + (scoredrawer.eaten * 200))
            return 4
        return 0
    def draw(self):
        # Рисуем пакмана (жёлтый прямоугольник)
        if not(self.rage_mod):
            pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.YELLOW)
        else:
            pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.WHITE)
    def game(self, scoredrawer: ScoreDrawer):
        if self.x==280 and self.y==200:
            self.x=920
            self.y=560
            self.cellx = self.x // 40
            self.celly = self.y // 40
            self.set_direction("LEFT")
        if self.x==960 and self.y==560:
            self.x=240
            self.y=200
            self.cellx = self.x // 40
            self.celly = self.y // 40
            self.set_direction("LEFT")
        if pyray.is_key_down(pyray.KEY_W):
            #if int(Field_structure[self.celly - 1][self.cellx]) != 1:
            self.set_direction("UP")
        elif pyray.is_key_down(pyray.KEY_S):
            #if int(Field_structure[self.celly + 1][self.cellx]) != 1:
            self.set_direction("DOWN")
        elif pyray.is_key_down(pyray.KEY_A):
            #if int(Field_structure[self.celly][self.cellx - 1]) != 1:
            self.set_direction("LEFT")
        elif pyray.is_key_down(pyray.KEY_D):
            #if int(Field_structure[self.celly][self.cellx + 1]) != 1:
            self.set_direction("RIGHT")
        self.update(scoredrawer)
    def set_direction(self, direction):
        # Задание направления движения пакмана
        self.direction = direction