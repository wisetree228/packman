from objects.base import BaseObject
import pyray

class PinkyGhost(BaseObject):

    def __init__(self, x, y, speed, width=30, height=30, direction="LEFT"):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.direction = direction


    def draw(self):
        pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.PINK)

    def update(self):
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > pyray.get_screen_width():
            self.x = pyray.get_screen_width() - self.width
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > pyray.get_screen_height():
            self.y = pyray.get_screen_height() - self.height