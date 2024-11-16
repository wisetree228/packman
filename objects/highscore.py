import pyray as pr
class HighscoreTableDrawer:
    def __init__(self, highscore_data):
        self.highscore_data = highscore_data
    def draw_table(self):
        title_font_size = 30
        table_x = 50
        table_y = 20
        
        pr.draw_text("Highscore Table", table_x, table_y, title_font_size, pr.WHITE)