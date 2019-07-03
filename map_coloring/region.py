class Region:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color
        self.neighbours = []

    def __str__(self):
        str_neighbours = ', '.join((f'{n.name} {n.color}' for n in self.neighbours))
        return f'{self.name} {self.color}: {str_neighbours}'
