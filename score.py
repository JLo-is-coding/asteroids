class Score:
    def __init__(self):
        self.score = 0
        self.bonus_life_requirement = 500

    def add(self):
        self.score += 1
    
    def get_current_score(self):
        return self.score
    
    def get_bonus_life_requirement(self):
        return self.bonus_life_requirement
