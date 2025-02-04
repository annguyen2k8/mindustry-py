from .static_wall import StaticWall

class StaticTree(StaticWall):
    def __init__(self, name):
        super().__init__(name)
        self.variants = 0