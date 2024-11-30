import pyray
import raylib
from objects.highscore import HighscoreTableDrawer

from objects.text import Text
from scenes.base import BaseScene
from settings import Settings
from objects.figure import Button
from objects.images.pacman import Pacman
from objects.images.cells import Cell

class MenuScene(BaseScene):
    def __init__(self):
        self.new_game_button = Button(Settings.WIDTH // 2 -100, Settings.HEIGHT // 2 - 100, 250, 80, "New game")
        self.exit_button = Button(Settings.WIDTH // 2 - 100, Settings.HEIGHT // 2, 250, 80, "Exit")
        self.pacman = Pacman(Settings.WIDTH - 40, Settings.HEIGHT - 40)
        self.cell1 = Cell(0, 0, 0)
        self.cell2 = Cell(80, 0, 1)
        self.cell3 = Cell(160, 0, 2)
        self.cell4 = Cell(240, 0, 3)
        self.highscoredrawer = HighscoreTableDrawer(highscore_data=[ {'name':'vanya', 'score':'100000000'},
                                                                     {'name':'player2', 'score':'12334'},
                                                                     {'name':'player3', 'score':'1111'},
                                                                     {'name':'player4', 'score':'900'},
                                                                     {'name':'player5', 'score':'800'},
                                                                     {'name':'player6', 'score':'700'},
                                                                     {'name':'player7', 'score':'600'},
                                                                     {'name':'player8', 'score':'500'},
                                                                     {'name':'player9', 'score':'225'},
                                                                     {'name':'player10', 'score':'12'}])
        #self.new_game_text = Text(Settings.WIDTH // 2 - 70, Settings.HEIGHT // 2 - 100, "New game", 40)
        #self.exit_text = Text(Settings.WIDTH // 2 - 20, Settings.HEIGHT // 2, "Exit", 40)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.new_game_button)
        self.objects.append(self.exit_button)
        self.objects.append(self.pacman)
        self.objects.append(self.cell1)
        self.objects.append(self.cell2)
        self.objects.append(self.cell3)
        self.objects.append(self.cell4)
        #self.objects.append(self.new_game_text)
        #self.objects.append(self.exit_text)
    def additional_process_event(self):
        #self.pacman.game()
        if self.exit_button.check_click():
            pyray.close_window()
        if self.new_game_button.check_click():
            Settings.set_game_scene()
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        # elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
        #     Settings.set_game_scene()
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_settings_scene()
