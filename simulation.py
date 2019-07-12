from bank import Bank
from player import Player


if __name__ == '__main__':

    n = input('Please enter the number of players in a simulation: ')
    players = []
    playersp = []
    for i in n:
        a = Player(i,playersp)
        playersp.append(a)
        players.append(a)
    bank = Bank(len(playersp), n)
    constructions = []
    while bank.turn != n+1 or len(playersp) != 1:

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