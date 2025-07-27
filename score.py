class Score:
    def __init__(self):
        self.score = 0

    def add(self):
        self.score += 1
    
    def get_current_score(self):
        return self.score