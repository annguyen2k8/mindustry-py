from mindustry.world.meta import *
from mindustry.graphics import *

from ...block import Block

class Radar(Block):
    iscoveryTime:float = 60.0 * 10.0
    rotateSpeed:float = 2.0
    
    glowColor:Color = Pal.turretHeat
    glowScl: float = 5.0
    glowMag: float = 0.6
    
    def __init__(self, name):
        super().__init__(name)
        self.update = self.solid = True
        self.flags = set(BlockFlag.hasFogRadius)
        self.outlineIcon = True
        self.fogRadius = 10