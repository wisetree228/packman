import pyray

class ScoreDrawer:
    def __init__(self, initial_score=0, x=0,y=0, font_size=30, color=pyray.WHITE):
        self.score = initial_score
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
        self.eaten = 0

    def update_score(self, new_score):
        self.score = new_score
    def draw(self):
        score_text = f'Your score: {self.score}'
        pyray.draw_text(score_text, self.x, self.y, self.font_size, self.color)
