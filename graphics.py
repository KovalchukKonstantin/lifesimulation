from flexx import flx


class Pl(flx.PyWidget):

    def init(self, player):

        self.player = player
        with flx.VBox():
            flx.Label(style='background:#cfc;', wrap =1, text = 'Current state of your resources')
            with flx.HSplit(flex=1):
                with flx.VBox():
                    self.name = flx.Label(text=f'Player name: {self.player.num}')
                    self.cash = flx.Label(text=f'Cash: {self.player.cash}')
                    self.rmu = flx.Label(text=f'RMUs: {self.player.rmu}')
                    self.fiu = flx.Label(text=f'FIUs: {self.player.fiu}')
                    self.sf = flx.Label(text=f'SFs: {self.player.sf}')
                    self.af = flx.Label(text=f'AFs: {self.player.af}')
                    self.bankrupt = flx.Label(text=f'Bankruptcy: {self.player.bankrupt}')


    def update_layout(self):
        self.name.set_text(self.player.name)
        self.cash.set_text(self.player.cash)
        self.rmu.set_text(self.player.rmu)
        self.fiu.set_text(self.player.fiu)
        self.sf.set_text(self.player.sf)
        self.af.set_text(self.player.af)
        self.bankrupt.set_text(self.player.bankrupt)



class Bankg(flx.PyWidget):

    def init(self, bank):
        self.bank = bank
        with flx.VBox():
            flx.Label(style='background:#cfc;', wrap = 1, text = 'Current state of the bank')
        with flx.HSplit(flex=1):
            with flx.VBox():
                self.lvl = flx.Label(text = f'Current bank level: {self.bank.lvl}')
                self.rmu = flx.Label(text = f'RMUs to sell: {self.bank.rmu}')
                self.rmup = flx.Label(text = f'Minimum buying price: {self.bank.rmup}')
                self.fiu = flx.Label(text = f'FIUs to buy: {self.bank.fiu}')
                self.fiup = flx.Label(text= f'Maximum buying price: {self.bank.fiup}')

    def update_b(self):
        self.lvl.set_text(self.bank.lvl)
        self.rmu.set_text(self.bank.rmu)
        self.rmup.set_text(self.bank.rmup)
        self.fiu.set_text(self.bank.fiu)
        self.fiup.set_text(self.bank.fiup)


