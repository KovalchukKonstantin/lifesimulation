
class Construction:
    def __init__(self, player, type):
        self.player = player
        self.type = type
        self.cost
        self.length
        if self.type == 1:
            self.length = 5
            self.cost = 5000
        elif self.type == 2:
            self.length = 7
            self.cost = 10000
        else:
            self.length = 9
            self.cost = 7000