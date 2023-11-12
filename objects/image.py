from objects.base import BaseObject


class Image(BaseObject):
    def __init__(self, x, y, path, size):
        super().__init__(x, y)
        self.path = path
        self.size = size