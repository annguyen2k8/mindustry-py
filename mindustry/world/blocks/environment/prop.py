from mindustry.graphics import *
from mindustry.world.block import *

class Prop(Block):
    layer:float = Layer.blockProp
    
    def __init__(self, name):
        super().__init__(name)
        self.breakable = True
        self.alwaysReplace = True
        self.instantDeconstruct = True