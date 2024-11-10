import pyray
import raylib

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings


class MenuScene(BaseScene):
    def __init__(self):
        self.hello_text = Text(Settings.WIDTH // 2, Settings.HEIGHT // 2, "Welcome", 32)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.hello_text)

    def additional_process_event(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_game_scene()
