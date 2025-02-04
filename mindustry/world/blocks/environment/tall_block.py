from mindustry.world.block import Block
from mindustry.graphics import *

class TallBlock(Block):
    shadowOffset:float = -3.0
    layer:float = Layer.power + 1
    shadowLayer:float = Layer.power - 1
    rotationRand:float = 20.0
    shadowAlpha:float = 0.6
    def __init__(self, name):
        super().__init__(name)
        self.solid = True
        self.clipSize = 90
        self.customShadow = True