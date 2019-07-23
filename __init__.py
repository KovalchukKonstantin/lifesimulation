from business_sim.bank import Bank
from business_sim.producer import Producer
from random import randint
from business_sim.human import Human


def sorting(a):
    return a.net_worth(bank, constructions)

if __name__ == '__main__':

    n = int(input('Please enter the number of players in a simulation: '))
    senior_player = 0
    active_players = n
    players = []

    turn = 1
    c = input('Do you want to have a human player in a simulation? y/N')
    if c == 'y':
        p = randint(1, n+1)
        for i in range (1,p):
            a = Producer(i)
            players.append(a)
        player = Human(p)
        players.append(player)
        for i in range (p+1, n+1):
            a = Producer(i)
            players.append(a)
    else:
        for i in range (1, n+1):
            a = Producer(i)
            players.append(a)
    bank = Bank(active_players)
    constructions = []
    while turn < n+1 and active_players > 1:
        for i in range(senior_player, len(players)):
            if not players[i].bankrupt:
                players[i].pay_fe()
        for i in range(senior_player):
            if not players[i].bankrupt:
                players[i].pay_fe()
        print(f'Players payed their fees on turn {turn}')
        for i in players:
            if not i.bankrupt:
                i.supply_bid(bank)
        bank.make_bids(senior_player)
        for i in range(senior_player, len(players)):
            if not players[i].bankrupt:
                players[i].produce_action()
        for i in range(senior_player):
            if not players[i].bankrupt:
                players[i].produce_action()
        for i in players:
            if not i.bankrupt:
                i.sell_bid(bank)
        bank.sell_auction(senior_player)
        for i in players:
            if not i.bankrupt:
                i.pay_i()
        print(f'Loan interests on turn {turn} were paid')
        for i in players:
            if not i.bankrupt:
                i.pay_l()
        print(f'Loans due on the turn {turn} were paid')
        for i in players:
            if not i.bankrupt:
                i.loan_take()
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
        for i in players:
            if not i.bankrupt:
                i.const(constructions)
        active_players = sum((1 for p in players if not p.bankrupt))
        if active_players > 1:
            bank.update_m(active_players)
            senior_player = next((s for s in ((i + senior_player + 1) % n for i in range(n))
                                  if not players[s].bankrupt))
            turn += 1
            print(f'The bank was updated. New Bank level is {bank.lvl}')
        elif active_players == 1:
            print('The game ended with a winner')
            break
        else:
            print('Everyone went bankrupt!!')
            break
    for i in players:
        if not i.bankrupt:
            print(str(i.num) + ' ' + str(i.net_worth(bank, constructions)))