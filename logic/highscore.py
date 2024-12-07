class HighscoreTable:
    def __init__(self, filename="highscores.txt", max_scores=10):
        self.filename = filename
        self.max_scores = max_scores
        self.scores = []
        self.load_scores()

    def load_scores(self):
        pass

    def saves_scores(self):
        pass

    def add_score(self, player_name, player_score):
        if len(self.scores) < self.max_scores or player_score > self.scores[-1][1]:
            self.scores.append((player_name, player_score))
            self.scores.sort(reverse = True)
            if len(self.scores) > self.max_scores:
                self.scores.pop()

    def get_top_scores(self):
        return self.scores

def get_highscore_data():
    d = []
    with open('logic/highscores.txt') as f:
        for s in f.readlines():
            a = {}
            name, count = s.split('=')
            d.append({'name':name, 'score':count})
    return d





if __name__ == "__main__":
    highscore_table = HighscoreTable()