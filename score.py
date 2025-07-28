class Score:
    def __init__(self):
        self.score = 0
        self.bonus_tracker = 0

    def add(self):
        self.score += 1
        self.bonus_tracker += 1
    
    def get_current_score(self):
        return self.score
    
    def get_current_bonus(self):
        return self.bonus_tracker
    
    def reset_bonus(self):
        self.bonus_tracker = 0