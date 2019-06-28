from region1 import *

def color(region,colors, regions_colored):
    for i in colors:
        if i not in region.neighbour_colors:
            region.color = i
            regions_colored+=1
            return True
    return False


def loop(region, regions_colored, num, colors):
    color(region, colors)
    if regions_colored == num:
        return True
    for i in region.neighbours:
        loop(i, regions_colored, num, colors)




if __name__=='__main__':
    map = RegionMap()
    region_list = map.parse('map.txt')
    for i in region_list:
        i.neighbour_c()
    colors = [0]
    regions_colored = 0
    num = len(region_list)
    loop(region_list)


