from mindustry.graphics import *
from mindustry.world import *

class Incinerator(Block):
    flameColor:Color = Color.valueOf("ffad9d")
    
    def __init__(self, name):
        super().__init__(name)
        self.hasPower = True
        self.hasLiquids = True
        self.update = True
        self.solid = True