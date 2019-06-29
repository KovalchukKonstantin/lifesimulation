import json


class Region:
    def __init__(self, name, color = None):
        self.name = name
        self.color = color
        self.neighbours = []


    def __str__(self):
        return f'{self.name} {self.color}: {self.neighbours}'



class RegionMap:
    def __init__(self):
        self._regions = {}

    def parse(self, filename):
        a = []
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
            for name, neighbours in data.items():
                #if name in self._regions:
                   # raise ValueError(f'Duplicate region name found {name}')\
                if not self._regions.get(name):
                    region = Region(name)
                    a.append(region)
                    self._regions[name] = region
                if neighbours:
                    for n_name in neighbours:
                        neighbour = self._regions.get(n_name)
                        if not neighbour:
                            neighbour = Region(n_name)
                            self._regions[n_name] = neighbour
                            a.append(neighbour)
                        self._regions.get(name).neighbours.append(neighbour)

        except Exception as e:
            print(f'Unable to load {filename}: {e!s}')
        return a



if __name__ == '__main__':
    map = RegionMap()
    map.parse('map.txt')
   # for region in map._regions:
       # print(region)