
class Region():
    def __init__(self, num, neighbours, color):
        self.num = num
        self.neighbours = neighbours
        self.color = color
        self.neighbour_colors = []
        for i in self.neighbours:
            self.neighbour_colors.append(i.color)

def create_regions(regions, neighbours):
    b = []
    for i in range(len(regions)):
        b.append(Region(regions[i], neighbours[i], None))
    return b


def change(region, colors_assigned, regions_colored, nregions, colors, sequence):
    if len(sequence == 0):
        colors.append(len(colors))
        tryc(region)
    old = region.color
    for i in range(len(colors)):
        if (colors[i]!=region.color and colors[i] not in region.neighbour_colors):
            region.color = colors[i]
            for i in range(region.neighbours):
                if region.neighbours[i].color == None:
                    tryc(region.neighbours[i], colors_assigned, regions_colored, nregions, colors, sequence)
            break
    if region.color == old:
        regions_colored-=1
        if regions_colored == 0:
            colors.append(len(colors))
            first = sequence[len(sequence)]
            sequence.pop()
            tryc(first,colors_assigned, regions_colored, nregions, colors, sequence)
        sequence.pop()
        change(sequence[len(sequence)-1],colors_assigned, regions_colored, nregions, colors, sequence)


def tryc(region, regions_colored, nregions, colors, sequence):
    if regions_colored<nregions:
        for i in range(len(colors)):
             if(colors[i] not in region.neighbour_colors):
                region.color = colors[i]
                regions_colored+=1
                sequence.append(region)
                for i in range(region.neighbours):
                    if region.neighbours[i].color == None:
                        tryc(region.neighbours[i], colors, regions_colored,nregions, colors, sequence)
                break
        if region.color == None:
            change(sequence[len(sequence)-1], colors, regions_colored, nregions, colors, sequence)




def main():
    my_regions = create_regions(regions, neighbours)
    colors = []
    nregions = len(my_regions)
    regions_colored = 0
    sequence = []
    tryc(my_regions[0], regions_colored, nregions, colors, sequence)
    if regions_



 if __name__ == "__main__":
     main()
