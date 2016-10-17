class Polyline:
    def __init__(self, start):
        self.points = [start]
    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.points[key]
        elif isinstance(key, int):
            return self.points[key]
        raise ValueError

pl = Polyline(9)

pl.points.append(3)
pl.points.append(4)

print(pl[0:2])