from business_sim.player import Player

class Human(Player):
    def supply_bid(self, bank):
        a = int(input('Enter the amount of units to bid on: '))
        b = int(input('Enter the price of a single unit: '))
        self.make_b(a, b, bank)

    def produce_action(self):
        s = []
        for i in range (1, self.sf+1):
            s.append(i)
        a = []
        for i in range (1, self.af+1):
            a.append(i)
        answer = ' '
        while len(s)+len(a) > 0:
            answer = input("Do you want to produce on your automated factory or on a standart one? A/s. Or enter q to stop production requests")
            if answer=='q':
                break
            if answer == 's':
                num = int(input('Please enter the number of a factory: '))
                if num in s:
                    self.prod_s(num)
                    s.remove(num)
                else:
                    print('This factory is either used or non existent')
            else:
                anum = int(input('Please enter the number of an automated factory: '))
                if anum in a:
                    v = int(input('How many units do you want to produce on this factory? 1/2 '))
                    self.prod_a(anum, v)
                    a.remove(anum)
                else:
                    print('This automated factory is either used or non existent')


    def sell_bid(self, bank):
        num = int(input('Please enter the amount of fius you want to sell: '))
        pr = int(input('Please enter the price for one fiu: '))
        self.sell(num, pr, bank)

    def loan_take(self):
        a = input('Do you want to take a loan? y/N ')
        if a == 'y':
            b = int(input('Enter the amount you want to loan: '))
            self.take_l(b)
    def const(self, constructions):
        a = input('Do you want to start a construction? y/N ')
        if a == 'y':
            b = int(input('Please enter the type of a construction you want to make: '))
            self.order_c(b, constructions)
