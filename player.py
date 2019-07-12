from loan import Loan
from construction import Construction
from bet import Bet

class Player:
    def __init__(self, num, players, sf = 2, rmu = 4, fiu = 2, cash = 10000, af = 0):
        self.num = num
        self.sf = sf
        self.af = af
        self.rmu = rmu
        self.fiu = fiu
        self.cash = cash
        self.lim = 2
        self.loans = []
        self.loan_am =  (self.sf * 5000 + af * 10000)/2
        self.bankrupt = False
        self.players = players

    def money_check(self):
        self.bankrupt = self.cash<0
        if self.bankrupt:
            self.players.remove(self)


    def pay_fe(self):
        self.cash = self.cash - self.rmu * 300 - self.fiu * 500 - self.sf * 1000 - self.af * 1500
        self.money_check()

    def prod_s(self, sf):
        if self.rmu>0 and self.cash>1999:
            self.rmu-=1
            self.cash-=2000
            self.fiu+=1
            print(f'Factory {sf} made a unit')
        else:
            print(f'Unit on factory {sf} was not produced due to the shortage of either money or raw materials')

    def make_b(self, am, price, bank):
        if price>= bank.rmup and price*am <= self.cash:
            a = Bet(self, self.num, am, price)
            bank.bidsi.append(a)
        else:
            print('You cannot make this bid right now')

    def prod_a(self, af, n):
        if n==1 and self.rmu>0 and self.cash>1999:
            self.rmu -= 1
            self.cash -= 2000
            self.fiu += 1
            print(f'Factory {af} made a unit')
            return True
        elif n==2 and self.rmu>1 and self.cash>2999:
            self.rmu -= 2
            self.cash -= 3000
            self.fiu += 2
            print(f'Factory {af} made two units')
            return True
        print(f'Factory {af} was unable to produce units requested')
        return False



    def sell(self, am, price, bank):
        if price < bank.fiup and am<=self.fiu:
            a = Bet(self, self.num, am, price)
            bank.bidsi.append(a)
        else:
            print('You cannot sell this much for this price right now')

    def pay_i(self):
        for i in self.loans:
            self.cash-=i.amount
            i.time_r-=1
        self.money_check()

    def pay_l(self):
        for i in self.loans:
            if i.time_r == 0:
                self.cash-=i.amount
                self.loan_am+=i.amount
                self.loans.remove(i)
        self.money_check()

    def take_l(self, amount):
        if amount<=self.loan_am:
            print('The loan has been taken')
            self.loan_am-=amount
            a = Loan(amount)
            self.cash+=amount
            self.loans.append(a)
        else:
            print('You cannot take this loan right now')

    def order_c(self, type, constructions):
        if type == 1 and self.cash > 2499 and self.lim<6:
            self.lim+=1
            self.cash-=2500
            a = Construction(self,1)
            constructions.append(a)
        elif type == 2 and self.cash > 4999 and self.lim<6:
            self.lim+=1
            self.cash-=5000
            a = Construction(self, 2)
            constructions.append(a)
        elif type == 3 and self.sf>0 and self.cash>3499 and self.lim<6:
            self.lim+=1
            self.cash-=3500
            a = Construction(self, 3)
