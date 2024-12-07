from scenes.base import BaseScene
from objects.highscore import HighscoreTableDrawer
from objects.figure import Button
from settings import Settings
import pyray
from logic.highscore import get_highscore_data


class HighscoreScene(BaseScene):
    def __init__(self):
        self.exit_button = Button(Settings.WIDTH // 2 - 100, Settings.HEIGHT // 2+200, 250, 80, "Exit")
        self.highscoredrawer = HighscoreTableDrawer(highscore_data=get_highscore_data())
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.exit_button)


    def additional_process_event(self):
        self.highscoredrawer.draw_table()
        if self.exit_button.check_click():
            Settings.set_scene(1)

