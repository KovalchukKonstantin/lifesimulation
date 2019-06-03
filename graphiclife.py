import arcade
from cell import *

class Life(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GREEN)

    def setup(self):
        cells = []
        b = create_cell_list()
        create_cells(b, cells)
        xar = []
        yar = []
        for t in range(len(cells)):
            xar.append(cells[t].x)
            yar.append(cells[t].y)
        xmin = min(xar)
        xmax = max(xar)
        ymin = min(yar)
        ymax = max(yar)
        field = make_field(cells, xmax, xmin, ymax, ymin)

    def on_draw(self):

        arcade.start_render()
        self.field.draw()
        arcade.finish_render()

    def update(self, delta_time):

        pass

def main():
    game = Life(800, 800)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()