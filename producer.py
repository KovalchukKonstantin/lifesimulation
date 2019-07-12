from player import Player

class Producer(Player):
    def supply_bid(self, bank):
        if bank.lvl == 1:
            self.make_b(2, 1000 ,bank)
        elif bank.lvl == 2:
            self.make_b(3,800,bank)
        elif bank.lvl == 3:
            self.make_b(4, 550, bank)
        elif bank.lvl == 4:
            self.make_b(5, 450, bank)
        else:
            self.make_b(6, 350, bank)


    def produce_action(self):
        for i in self.af:
            if self.prod_a(i, 2):
                continue
            self.prod_a(i,1)
        for i in self.sf:
            self.prod_s(i)

    def sell_bid(self, bank):
        if bank.lvl == 1:
            self.sell(self.fiu, 4000 ,bank)
        elif bank.lvl == 2:
            self.sell(self.fiu-1,4100,bank)
        elif bank.lvl == 3:
            self.sell(self.fiu-2, 4200, bank)
        elif bank.lvl == 4:
            self.sell(self.fiu-3, 4300, bank)
        else:
            self.sell(1, 6000, bank)

    def loan_take(self):
        pass

    def const(self):
        pass
