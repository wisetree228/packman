from objects.base import BaseObject
import pyray

class Cherry(BaseObject):
    def __init__(self, x, y, visible = True):
        self.x = x
        self.y = y
        self.visible = visible
        self.fps_of_living = 0

    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False

    def draw(self):
        if self.visible:
            pyray.draw_circle(self.x, self.y, 10, pyray.RED)

    def update(self):
        self.fps_of_living += 1
        if self.fps_of_living >=180:
            self.hide()


