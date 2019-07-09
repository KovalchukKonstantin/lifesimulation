import math
from random import randint

class Bank:
    def __init__(self, p):
        self.rmu = 2*p
        self.fiu = 2*p
        self.rmup = 500
        self.fiup = 5500
        self.lvl = 3
    def update_m(self,p):
        rd= randint(1,12)
        if self.lvl == 1:
            if rd in [1,2,3,4]:
                self.lvl = 1
            elif rd in [5,6,7,8]:
                self.lvl = 2
            elif rd in [9,10]:
                self.lvl = 3
            elif rd in [11]:
                self.lvl = 4
            else:
                self.lvl = 5
        elif self.lvl == 2:
            if rd in [1,2,3]:
                self.lvl = 1
            elif rd in [4,5,6]:
                self.lvl = 2
            elif rd in [7,8,9]:
                self.lvl = 3
            elif rd in [10,11]:
                self.lvl = 4
            else:
                self.lvl = 5
        elif self.lvl == 3:
            if rd in [1]:
                self.lvl = 1
            elif rd in [2,3,4]:
                self.lvl = 2
            elif rd in [5,6,7,8]:
                self.lvl = 3
            elif rd in [9,10,11]:
                self.lvl = 4
            else:
                self.lvl = 5
        elif self.lvl == 4:
            if rd in [1]:
                self.lvl = 1
            elif rd in [2,3]:
                self.lvl = 2
            elif rd in [4,5,6]:
                self.lvl = 3
            elif rd in [7,8,9,10]:
                self.lvl = 4
            else:
                self.lvl = 5
        else:
            if rd in [1]:
                self.lvl = 1
            elif rd in [2]:
                self.lvl = 2
            elif rd in [3,4]:
                self.lvl = 3
            elif rd in [5,6,7,8]:
                self.lvl = 4
            else:
                self.lvl = 5
        if self.lvl == 1:
            self.rmu = p
            self.fiu = 3 * p
            self.rmup = 800
            self.fiup = 6500
        elif self.lvl == 2:
            self.rmu = math.floor(1.5 * p)
            self.fiu = math.floor(2.5 * p)
            self.rmup = 650
            self.fiup = 6000
        elif self.lvl == 3:
            self.rmu = 2 * p
            self.fiu = 2 * p
            self.rmup = 500
            self.fiup = 5500
        elif self.lvl == 4:
            self.rmu = math.floor(2.5 * p)
            self.fiu = math.floor(1.5 * p)
            self.rmup = 400
            self.fiup = 5000
        else:
            self.rmu = 3 * p
            self.fiu = p
            self.rmup = 300
            self.fiup = 4500

