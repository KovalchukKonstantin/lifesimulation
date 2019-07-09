


if __name__ == '__main__':




    turn = 1
    p = n
    senior = (turn%2)+1
    constructions = []
    while turn != 13 or len(p) != 1:
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