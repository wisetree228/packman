from scenes.base import BaseScene
import pyray
import raylib
from settings import Settings
from objects.images.pacman import Pacman
from objects.field import FieldDrawer
from logic.field import Field
from objects.ghosts.blinky import BlinkyGhost
from objects.ghosts.pinky import PinkyGhost
from objects.ghosts.inky import InkyGhost
from objects.ghosts.clyde import ClydeGhost
from objects.cherry import Cherry

class GameScene(BaseScene):
    def __init__(self):
        self.pacman = Pacman(40, 560)
        self.objects = []
        self.set_up_objects()
        self.field = FieldDrawer(field=Field())
        self.redGhost = BlinkyGhost(40, 560, 2)
        self.pinkGhost = PinkyGhost(200, 200, 14)
        self.inkyGhost = InkyGhost(300, 300, 12)
        self.clydeGhost = ClydeGhost(400, 400, 11)
        self.cherry = Cherry(300, 300)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.pacman)



    def additional_process_event(self):
        self.pacman.game()
        self.field.draw()
        self.redGhost.game()
        self.redGhost.update()
        self.redGhost.draw()
        self.pinkGhost.update()
        self.pinkGhost.draw()
        self.inkyGhost.update()
        self.inkyGhost.draw()
        self.clydeGhost.update()
        self.clydeGhost.draw()
        self.cherry.update()
        self.cherry.draw()
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            Settings.set_game_scene()
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_settings_scene()