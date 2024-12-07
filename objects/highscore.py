import pyray as pr
class HighscoreTableDrawer:
    def __init__(self, highscore_data, text = "Table",table_x:int = 450 ,table_y:int = 150, tittle_font_size:int = 30):
        self.highscore_data = highscore_data
        self.text = text
        self.table_x = table_x
        self.table_y = table_y
        self.tittle_font_size = tittle_font_size
    def draw_table(self):
        pr.begin_drawing()
        pr.draw_text(self.text , self.table_x, self.table_y, self.tittle_font_size, pr.WHITE)
        pr.end_drawing()
        for i in range(len(self.highscore_data)):
            pr.draw_text(f'player: {self.highscore_data[i]["name"]}, record: {self.highscore_data[i]["score"]}', 350, 200+(i*30), 25, pr.WHITE)