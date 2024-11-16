from scenes.base import BaseScene
import pyray
import raylib
from settings import Settings
from objects.images.pacman import Pacman
from objects.field import FieldDrawer
from logic.field import Field
from objects.ghosts.blinky import BlinkyGhost
from objects.ghosts.pinky import PinkyGhost

class GameScene(BaseScene):
    def __init__(self):
        self.objects = []
        self.set_up_objects()
        self.pacman = Pacman(Settings.WIDTH - 40, Settings.HEIGHT - 40)
        self.field = FieldDrawer(field = Field())
        self.redGhost = BlinkyGhost(100, 100, 10)
        self.pinkGhost = PinkyGhost(200, 200, 14)
        super().__init__()

    #def set_up_objects(self):
        #self.objects.append(self.pacman)



    def additional_process_event(self):
        #self.pacman.game()
        self.field.draw()
        self.redGhost.update()
        self.redGhost.draw()
        self.pinkGhost.update()
        self.pinkGhost.draw()
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            Settings.set_game_scene()
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_settings_scene()