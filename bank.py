import math
from random import randint


def sorting(bid):
    return bid.name

class Bank:
    def __init__(self, p, n):
        self.rmu = 2*p
        self.fiu = 2*p
        self.rmup = 500
        self.fiup = 5500
        self.lvl = 3
        self.bidsi=[]
        self.turn = 1
        self.n = n
        self.senior = (self.turn%self.n)+1


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
        self.turn +=1


    def make_bids(self):
        prices = []
        names = []
        while len(self.bidsi) != 0 or self.rmu!=0:
            for i in self.bidsi:
                prices.append(i.price)
                names.append(i.name)
            maxv = 0
            max = []
            neg = []
            pos = []
            for i in range(len(prices)):
                if prices[i] > maxv:
                    max = [i]
                    maxv = prices[i]
                elif prices[i]== maxv:
                    max.append(i)
            for i in max:
                if names[i]-self.senior < 0:
                    neg.append(self.bidsi[i])
                else:
                    pos.append(self.bidsi[i])
            pos.sort(key = sorting)
            neg.sort(key = sorting)
            merged = pos + neg
            for i in merged:
                if i.num <= self.rmu:
                    i.player.rmu+=i.num
                    i.player.cash-=(i.num*i.price)
                    self.bidsi.remove(i)
                    self.rmu -= i.num
                    print(f'Player {i.player.num} got {i.num} rmus for the price of {i.price} each')
                else:
                    i.player.rmu+=self.rmu
                    i.player.cash-=(self.rmu*i.price)
                    print(f'Player {i.player.num} got {self.rmu} rmus for the price of {i.price} each')
                    self.bidsi.remove(i)
                    self.rmu = 0
            prices.clear()
            names.clear()
        self.bidsi.clear()

    def sell_auction(self):
        prices = []
        names = []
        while len(self.bidsi)!= 0 or self.fiu!=0:
            for i in self.bidsi:
                prices.append(i.price)
                names.append(i.name)
            minv = self.fiup
            min = []
            neg = []
            pos = []
            for i in range(len(prices)):
                if prices[i]<minv:
                    minv = prices[i]
                    min = [i]
                elif prices[i] == minv:
                    min.append(i)
            for i in min:
                if names[i] - self.senior < 0:
                    neg.append(self.bidsi[i])
                else:
                    pos.append(self.bidsi[i])
            pos.sort(key=sorting)
            neg.sort(key=sorting)
            merged = pos + neg
            for i in merged:
                if i.num <= self.fiu:
                    i.player.fiu-=i.num
                    i.player.cash+=(i.num*i.price)
                    print(f'Player {i.player.num} sold {i.num} fius for the price of {i.price} each')
                    self.bidsi.remove(i)
                    self.fiu-=i.num
                else:
                    i.player.fiu-=self.fiu
                    i.player.cash-=(self.fiu*i.price)
                    print(f'Player {i.player.num} sold {self.fiu} fius for the price of {i.price} each')
                    self.bidsi.remove(i)
                    self.fiu = 0
            prices.clear()
            names.clear()
        self.bidsi.clear()



