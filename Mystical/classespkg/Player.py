class Player:
    def __init__(self):
        #using self.skills to store skills as well as attack values in a dictionary 
        self.skills = {'Punch':2}
        self.gold = 10
        self.hp = 10
        self.level = 1
        self.defense = 0
        self.maxhp = self.hp + self.level - 1
