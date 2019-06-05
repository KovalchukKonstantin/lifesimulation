class Cell:
    """Represents a living cell that hold its coordinates and a number of neighbors"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = 0

    def get_neighbors(self, xmin, ymin):
        yield self.y - ymin, self.x - xmin
        yield self.y - ymin, self.x - xmin + 1
        yield self.y - ymin, self.x - xmin + 2
        yield self.y - ymin + 1, self.x - xmin
        yield self.y - ymin + 1, self.x - xmin + 2
        yield self.y - ymin + 2, self.x - xmin
        yield self.y - ymin + 2, self.x - xmin + 1
        yield self.y - ymin + 2, self.x - xmin + 2


def create_cell_list():
    """
    Create a plane list of intercolated x,y coordinates
    """
    a = input('Enter starting coordinates x,y for each cell separated by space: ')
    c = a.split()
    b = []
    for x in c:
        b.append(int(x))
    return b


def create_cells(coordinates):
    """
    Create a list of Cells from coordinates

    :param coordinates: a list of x,y coordinates
    :return:
    """
    return [Cell(coordinates[i], coordinates[i + 1])
            for i in range(0, len(coordinates), 2)]


def make_field(cells, xmax, xmin, ymax, ymin):
    field = [[0] * (xmax - xmin + 3) for _ in range(ymax - ymin + 3)]
    for t in cells:
        field[t.y - ymin + 1][t.x - xmin + 1] = t
    return field


def modify(a):
    if isinstance(a, Cell):
        a.neighbors += 1
    else:
        a += 1
    return a


def update_field(field, cells, xmin, ymin, xar, yar):
    for cell in cells:
        for x, y in cell.get_neighbors(xmin, ymin):
            field[y][x] = modify(field[y][x])
    for cell in range(len(field)):
        for i in range(len(field[0])):
            if isinstance(field[cell][i], Cell):
                if field[cell][i].neighbors < 2 or field[cell][i].neighbors > 3:
                    xar.remove(i + xmin - 1)
                    yar.remove(cell + ymin - 1)
                    cells.remove(field[cell][i])
                    field[cell][i] = 0
            else:
                if field[cell][i] == 3:
                    field[cell][i] = Cell(i + xmin - 1, cell + ymin - 1)
                    cells.append(field[cell][i])
                    xar.append(i + xmin - 1)
                    yar.append(cell + ymin - 1)
    ymin = min(yar)
    ymax = max(yar)
    xmin = min(xar)
    xmax = max(xar)
    field = make_field(cells, xmax, xmin, ymax, ymin)
    for cell in field:
        for i in cell:
            if isinstance(i, Cell):
                i.neighbors = 0
    return field, cells, xmin, ymin, xmax, ymax, xar, yar


def print_field(field):
    for i in range(len(field)):
        for t in range(len(field[0])):
            if isinstance(field[i][t], Cell):
                print("#", end=" ")
            else:
                print(' ', end=" ")
        print(" ")


if __name__ == '__main__':
    # initialize the state
    b = create_cell_list()
    cells = create_cells(b)
    xar = []
    yar = []
    # compile lists of x and y coordinates
    for t in cells:
        xar.append(t.x)
        yar.append(t.y)
    xmin = min(xar)
    xmax = max(xar)
    ymin = min(yar)
    ymax = max(yar)
    field = make_field(cells, xmax, xmin, ymax, ymin)
    print_field(field)
    # main loop
    while True:
        t = input("Press c to continue simulation. Press q to stop simulation: ")
        if (t == "q"):
            print("Life simulation is over")
            break
        elif (t == "c"):
            field, cells, xmin, ymin, xmax, ymax, xar, yar = update_field(field, cells, xmin, ymin,
                                                                          xar, yar)
            print_field(field)
        else:
            print("Please enter a valid command")
            continue
