from . import *

from mindustry.type import *

class OreBlock(OverlayFloor):
    def __init__(self, name:str=None, ore:Item=None):
        name = name if name else 'ore-' + ore.name
        super().__init__(name)
        
        if ore:
            self.itemDrop = ore
            self.mapColor.set(ore.color)
        self.variants = 3
        self.useColor = True
