from scenes.base import BaseScene
from objects.highscore import HighscoreTableDrawer
from objects.figure import Button
from settings import Settings
import pyray

class HighscoreScene(BaseScene):
    def __init__(self):
        self.exit_button = Button(Settings.WIDTH // 2 - 100, Settings.HEIGHT // 2+200, 250, 80, "Exit")
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
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.exit_button)


    def additional_process_event(self):
        self.highscoredrawer.draw_table()
        if self.exit_button.check_click():
            Settings.set_scene(1)

