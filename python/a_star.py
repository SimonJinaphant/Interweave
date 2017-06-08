class Tile:

    def __init__(self):
        self.g = 0
        self.h = 0
        self.cost = 0
        self.parent = None

        self.isOpen = False
        self.isClosed = False


class GridMap:
