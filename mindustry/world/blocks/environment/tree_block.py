from mindustry.world import *

class TreeBlock(Block):
    shadowOffset:float = -4.0
    def __init__(self, name):
        super().__init__(name)
        self.solid = True
        self.clipSize = 90
        self.customShadow = True