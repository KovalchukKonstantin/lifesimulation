from bank import Bank
from producer import Producer


def sorting(a):
    return a.net_worth(bank, constructions)

if __name__ == '__main__':

    n = int(input('Please enter the number of players in a simulation: '))
    players = []
    playersp = []
    for i in range (1, n+1):
        a = Producer(i,playersp)
        playersp.append(a)
        players.append(a)
    bank = Bank(len(playersp), n)
    constructions = []
    while bank.turn != n+1 or len(playersp) != 1:
        for i in range(bank.senior, len(playersp)):
            playersp[i].pay_fe()
        for i in range(bank.senior):
            playersp[i].pay_fe()
        print(f'Players played their fees on turn {bank.turn}')
        for i in range(len(playersp)):
            playersp[i].supply_bid(bank)
        bank.make_bids()
        for i in range(bank.senior, len(playersp)):
            playersp[i].produce_action()
        for i in range(bank.senior):
            playersp[i].produce_action()
        for i in range(len(playersp)):
            playersp[i].sell_bid(bank)
        bank.sell_auction()
        for i in range(len(playersp)):
            playersp[i].pay_i()
        print(f'Loan interests on turn {bank.turn} were paid')
        for i in range(len(playersp)):
            playersp[i].pay_l()
        print(f'Loans due on the turn {bank.turn} were paid')
        for i in range(len(playersp)):
            playersp[i].loan_take()
        for i in constructions:
            if i.length == 1:
                if i.type == 1:
                    i.player.cash-=2500
                    i.player.sf+=1
                    constructions.remove(i)
                elif i.type == 2:
                    i.player.cash-=5000
                    i.plater.af+=1
                    constructions.remove(i)
                else:
                    i.player.cash-=3500
                    i.player.sf-=1
                    i.player.af+=1
                    constructions.remove(i)
            else:
                i.length-=1
        for i in range(len(playersp)):
            playersp[i].const()
        bank.update_m(len(playersp))
        print(f'The bank was updated. New Bank level is {bank.lvl}')
    playersp.sort(key = sorting)
    for i in playersp:
        print(i.net_worth(bank, constructions))
   # for i in playersp:
      #  print(i.net_worth(bank,constructions))