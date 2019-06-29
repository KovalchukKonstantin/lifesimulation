from region1 import *

def color(region, colors):
    neighbour_colors = set()
    for neighbour in region.neighbours:
        if neighbour.color is not None:
            neighbour_colors.add(neighbour.color)
    available_colors = set(colors)-neighbour_colors
    if len(available_colors) == 0:
        return False
    sorted_available_colors = list(available_colors)
    sorted_available_colors.sort()
    if region.color is None:
        region.color = sorted_available_colors[0]
        return True
    for color in sorted_available_colors:
        if region.color<color:
            region.color = color
            return True
    return False

def loop(region, num, colors, sequence):
    if color(region, colors):
        sequence.append(region)
        for new_region in region.neighbours:
            if new_region not in sequence:
                while not loop(new_region, num, colors, sequence):
                    if not color(region, colors):
                        if region == sequence[0]:
                            colors.append(len(colors))
                        else:
                            sequence.pop()
                            return False

        return True
    else:
        return False



if __name__=='__main__':
    map = RegionMap()
    region_list = map.parse('map.txt')
    colors = [0]
    num = len(region_list)
    sequence = []
    loop(region_list[0], num, colors, sequence)
    for i in region_list:
        print(i)


