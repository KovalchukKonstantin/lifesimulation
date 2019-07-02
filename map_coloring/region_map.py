import json

from .region import Region


class RegionMap:
    def __init__(self):
        self._regions = {}

    def parse(self, filename):
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
            for name, neighbours in data.items():
                # if name in self._regions:
                # raise ValueError(f'Duplicate region name found {name}')\
                region = self._regions.get(name)
                if not region:
                    region = Region(name)
                    self._regions[name] = region
                if neighbours:
                    for n_name in neighbours:
                        neighbour = self._regions.get(n_name)
                        if not neighbour:
                            neighbour = Region(n_name)
                            self._regions[n_name] = neighbour
                        region.neighbours.append(neighbour)
        except Exception as e:
            print(f'Unable to load {filename}: {e!s}')
        return list(self._regions.values())
