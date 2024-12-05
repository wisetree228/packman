class ScoreCounter:
    def __init__(self, initial_score:int = 0):
        self.score = initial_score
    def add(self, x):
        self.score += x
    def get_score(self):
        return self.score

