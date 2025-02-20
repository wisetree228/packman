from scenes.base import BaseScene
import pyray
import raylib
from settings import Settings
from objects.images.pacman import Pacman
from objects.field import FieldDrawer
from objects.score import ScoreDrawer
from logic.field import Field
from objects.ghosts.blinky import BlinkyGhost
from objects.ghosts.pinky import PinkyGhost
from objects.ghosts.inky import InkyGhost
from objects.ghosts.clyde import ClydeGhost
from objects.cherry import Cherry
from objects.figure import Button
from objects.life import Life

Pause = True
class GameScene(BaseScene):
    def __init__(self):
        self.pacman = Pacman(40, 560)
        self.objects = []
        self.set_up_objects()
        self.field = FieldDrawer(field=Field())
        self.redGhost = BlinkyGhost(360, 280, 2)
        self.pinkGhost = PinkyGhost(400, 280, 2)
        self.inkyGhost = InkyGhost(360, 280, 2)
        self.clydeGhost = ClydeGhost(400, 280, 2)
        self.exit_menu_button = Button(Settings.WIDTH // 2 - 150, 300, 300, 80, "Back to menu", raylib.YELLOW)
        self.cherry = Cherry(300, 300)
        self.life_counter = Life(40, 680, 50, 3)
        self.scoredrawer = ScoreDrawer(x=400, y=700)
        super().__init__()

    def set_up_objects(self):
        self.objects.append(self.pacman)




    def additional_process_event(self):
        global Pause
        self.pacman.game(self.scoredrawer)
        self.field.draw()
        self.redGhost.update()
        self.redGhost.draw()
        self.redGhost.game()
        self.pinkGhost.update()
        self.pinkGhost.draw()
        self.pinkGhost.game()
        self.inkyGhost.update()
        self.inkyGhost.draw()
        self.inkyGhost.game()
        self.clydeGhost.update()
        self.clydeGhost.draw()
        self.clydeGhost.game()
        self.cherry.update()
        self.cherry.draw()
        self.life_counter.draw()
        self.field.eat(self.pacman, self.scoredrawer)
        self.scoredrawer.draw()
        self.check_win()
        self.wr=False
        if self.life_counter.count_hp==0:
            Pause = False
            pyray.draw_text("YOU LOSE", 300, 200, 80, pyray.RED)
            self.pacman.speed = 0
            self.redGhost.speed = 0
            self.pinkGhost.speed = 0
            self.inkyGhost.speed = 0
            self.clydeGhost.speed = 0
        if self.pacman.ghost_collision(self.clydeGhost, self.inkyGhost, self.pinkGhost, self.redGhost, self.scoredrawer)!=0:
            if not self.pacman.rage_mod:
                self.life_counter.count_hp-=1
                self.pacman = Pacman(40, 560)
                self.objects = []
                self.set_up_objects()
                self.redGhost = BlinkyGhost(360, 280, 2)
                self.pinkGhost = PinkyGhost(400, 280, 2)
                self.inkyGhost = InkyGhost(360, 280, 2)
                self.clydeGhost = ClydeGhost(400, 280, 2)
                self.exit_menu_button = Button(Settings.WIDTH // 2 - 150, 300, 300, 80, "Back to menu", raylib.YELLOW)
            else:
                if self.pacman.ghost_collision(self.clydeGhost, self.inkyGhost, self.pinkGhost, self.redGhost, self.scoredrawer)==1:
                    self.clydeGhost.death(self.scoredrawer)
                if self.pacman.ghost_collision(self.clydeGhost, self.inkyGhost, self.pinkGhost, self.redGhost, self.scoredrawer)==2:
                    self.inkyGhost.death(self.scoredrawer)
                if self.pacman.ghost_collision(self.clydeGhost, self.inkyGhost, self.pinkGhost, self.redGhost, self.scoredrawer)==3:
                    self.pinkGhost.death(self.scoredrawer)
                if self.pacman.ghost_collision(self.clydeGhost, self.inkyGhost, self.pinkGhost, self.redGhost, self.scoredrawer)==4:
                    self.redGhost.death(self.scoredrawer)
        if not Pause:
            self.exit_menu_button.draw()
            if self.exit_menu_button.check_click():
                Settings.set_scene(1)
                Pause = True
                self.pacman = Pacman(40, 560)
                self.objects = []
                self.set_up_objects()
                self.field = FieldDrawer(field=Field())
                self.redGhost = BlinkyGhost(360, 280, 2)
                self.pinkGhost = PinkyGhost(400, 280, 2)
                self.inkyGhost = InkyGhost(360, 280, 2)
                self.clydeGhost = ClydeGhost(400, 280, 2)
                self.exit_menu_button = Button(Settings.WIDTH // 2 - 150, 300, 300, 80, "Back to menu", raylib.YELLOW)
                self.cherry = Cherry(300, 300)
                self.life_counter = Life(40, 680, 50, 3)
                self.scoredrawer = ScoreDrawer(x=400, y=700)
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            if Pause:
                self.pacman.speed = 0
                self.redGhost.speed = 0
                self.pinkGhost.speed = 0
                self.inkyGhost.speed = 0
                self.clydeGhost.speed = 0
                Pause = False
            else:
                self.pacman.speed = 5
                self.redGhost.speed = 2
                self.pinkGhost.speed = 2
                self.inkyGhost.speed = 2
                self.clydeGhost.speed = 2
                Pause = True
            #Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            Settings.set_scene(1)
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            Settings.set_game_scene()
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_THREE):
            Settings.set_settings_scene()

    def check_win(self):
        if len(self.field.seeds)+len(self.field.energ) == 0:
            self.pacman.speed = 0
            self.redGhost.speed = 0
            self.inkyGhost.speed = 0
            self.pinkGhost.speed = 0
            self.clydeGhost.speed = 0
            Pause = False
            self.exit_menu_button.draw()
            pyray.draw_text(f'YOU WON! YOUR SCORE IS {self.scoredrawer.score}', 100, 200, 50, pyray.GREEN)
            if not(self.wr):
                with open('logic/highscores.txt', 'a') as f:
                    f.write(f'\nYou={self.scoredrawer.score}')
                    self.wr = True
            if self.exit_menu_button.check_click():
                Settings.set_scene(1)
                Pause = True
                self.pacman = Pacman(40, 560)
                self.objects = []
                self.set_up_objects()
                self.field = FieldDrawer(field=Field())
                self.redGhost = BlinkyGhost(360, 280, 2)
                self.pinkGhost = PinkyGhost(400, 280, 2)
                self.inkyGhost = InkyGhost(360, 280, 2)
                self.clydeGhost = ClydeGhost(400, 280, 2)
                self.exit_menu_button = Button(Settings.WIDTH // 2 - 150, 300, 300, 80, "Back to menu", raylib.YELLOW)
                self.cherry = Cherry(300, 300)
                self.life_counter = Life(40, 680, 50, 3)
                self.scoredrawer = ScoreDrawer(x=400, y=700)