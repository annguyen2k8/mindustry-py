from . import *

class StaticTree(StaticWall):
    def __init__(self, name):
        super().__init__(name)
        self.variants = 0