from scenes.base import BaseScene
import pyray
from settings import Settings

class SettingsScene(BaseScene):
    def __init__(self):
        self.objects = []
        self.set_up_objects()

    def additional_process_event(self):

        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            Settings.set_game_scene()
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_settings_scene()