from . import *

class ShieldWall(Wall):
    def __init__(self, name):
        super().__init__(name)
        self.update = True