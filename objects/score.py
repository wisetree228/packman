import pyray

class ScoreDrawer:
    def __init__(self, initial_score=0, x=0,y=0, font_size=20, color=pyray.BLACK):
        self.score = initial_score
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color

    def update_score(self, new_score):
        self.score = new_score
    def draw(self):
        score_text = self.score
        pyray.draw_text(self.text, self.x, self.y, self.font_size, self.color)
