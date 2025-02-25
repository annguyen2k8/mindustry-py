from mindustry.graphics import *
from mindustry.world import *


class Accelerator(Block):
    # launchBlock = Blocks.coreNucleus
    lightColor:Color = Color.valueOf("eab678")
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True
        self.hasItems = True
        self.hasPower = True
        self.itemCapacity = 8000
        self.configurable = True
        self.flags = set().add(BlockFlag.launchPad)