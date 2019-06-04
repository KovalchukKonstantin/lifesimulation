
class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.neighbours = 0

cells = []

def create_cell_list():
    a = input('Enter starting coordinates x,y for each cell sparated by space: ')
    c = a.split()
    b = []
    for x in c:
        b.append(int(x))
    return b
def create_cells(coordinates, cells):
    i = 0
    while(i<len(coordinates)):
        cells.append(Cell(coordinates[i],coordinates[i+1]))
        i+=2
    return cells
b = create_cell_list()
cells = create_cells(b,cells)


xar = []
yar = []
for t in cells:
    xar.append(t.x)
    yar.append(t.y)
xmin = min(xar)
xmax = max(xar)
ymin = min(yar)
ymax = max(yar)

def make_field(cells, xmax, xmin, ymax, ymin):
    field = [[0]*(xmax-xmin+3) for i in range (ymax-ymin+3)]
    #for i in range(len(cells)):
        #field[cells[i].y-ymin+1][cells[i].x-xmin+1] = cells[i]
    for t in cells:
        field[t.y-ymin+1][t.x-xmin+1] = t
    #for i in range(len(xar)):
    #    field[yar[i]-ymin+1][xar[i]-xmin+1] = Cell(xar[i],yar[i])
    return field

field = make_field(cells, xmax, xmin, ymax, ymin)

def modify(a):
    if isinstance(a, Cell):
        a.neighbours+=1
    else:
        a+=1
    return a

def update_field(field, cells, xmin, ymin, xmax, ymax, xar, yar):
    field = [[0] * (xmax - xmin + 3) for i in range(ymax - ymin + 3)]
    for t in cells:
        field[t.y-ymin+1][t.x-xmin+1] = t
    for t in field:
        for i in t:
            if isinstance(i, Cell):
                i.neighbours = 0
            else:
                i = 0
    for t in cells:
            field[t.y-ymin][t.x-xmin] = modify(field[t.y-ymin][t.x-xmin])
            field[t.y-ymin][t.x-xmin+1]= modify(field[t.y-ymin][t.x-xmin+1])
            field[t.y-ymin][t.x-xmin+2] = modify(field[t.y-ymin][t.x-xmin+2])
            field[t.y-ymin+1][t.x-xmin] = modify(field[t.y-ymin+1][t.x-xmin])
            field[t.y-ymin+1][t.x-xmin+2] = modify(field[t.y-ymin+1][t.x-xmin+2])
            field[t.y-ymin+2][t.x-xmin] = modify(field[t.y-ymin+2][t.x-xmin])
            field[t.y-ymin+2][t.x-xmin + 1] = modify(field[t.y-ymin+2][t.x-xmin + 1])
            field[t.y-ymin+2][t.x-xmin + 2] = modify(field[t.y-ymin+2][t.x-xmin + 2])
    for t in range(len(field)):
        for i in range(len(field[0])):
            if isinstance(field[t][i], Cell):
                if (field[t][i].neighbours<2 or field[t][i].neighbours>3):
                    xar.remove(i-xmin+1)
                    yar.remove(t-ymin+1)
                    cells.remove(field[t][i])
                    field[t][i] = 0
            else:
                if (field[t][i] == 3):
                    field[t][i] = Cell(i,t)
                    cells.append(field[t][i])
                    xar.append(i)
                    yar.append(t)
    ymin = min(yar)
    ymax = max(yar)
    xmin = min(xar)
    xmax = max(xar)
    return field, cells, xmin, ymin, xmax, ymax, xar, yar
def print_field(field):
    for i in range(len(field)):
        for t in range(len(field[0])):
            if isinstance(field[i][t],Cell):
                print("C", end=" ")
            else:
                print(field[i][t], end=" ")
        print(" ")

print_field(field)

while True:
    t = input("Press c to continue simulation. Press q to stop simulation: ")
    if (t == "q"):
        print("Life simulation is over")
        break
    elif (t == "c"):
        field, cells, xmin, ymin, xmax,ymax, xar, yar = update_field(field, cells, xmin, ymin, xmax, ymax, xar, yar)
        print_field(field)
    else:
        print ("Please enter a valid command")
        continue

# while True:
#         if keyboard.is_pressed('q'):
#             print('The simulation is over')
#             break
#         if keyboard.is_pressed('Space'):
#             update_field(field, xmin, ymin)