from mindustry.graphics import *

from ...block import *

class MendProjector(Block):
    baseColor:Color = Color.valueOf("84f491")
    phaseColor:Color = baseColor
    reload:float = 250.0
    range:float = 60.0
    healPercent:float = 12.0
    phaseBoost:float = 12.0
    phaseRangeBoost:float = 50.0
    useTime:float = 400.0
    
    def __init__(self, name):
        super().__init__(name)
        self.solid = True
        self.update = True
        self.group = BlockGroup.projectors
        self.hasPower = True
        self.hasItems = True
        self.emitLight = True
        self.lightRadius = 50.0
        self.suppressable = True
        self.envEnabled |= Env.space