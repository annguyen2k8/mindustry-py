from mindustry.graphics import *
from mindustry.world import *
from mindustry.world.meta import *

class OverdriveProjector(Block):
    reload:float = 60.0
    range:float = 80.0
    speedBoost:float = 1.5
    speedBoostPhase:float = 0.75
    useTime:float = 400.0
    phaseRangeBoost:float = 20.0
    hasBoost:bool = True
    baseColor:Color = Color.valueOf("feb380")
    phaseColor:Color = Color.valueOf("ffd59e")
    
    def __init__(self, name):
        super().__init__(name)
        self.solid = True
        self.update = True
        self.group = BlockGroup.projectors
        self.hasPower = True
        self.hasItems = True
        self.canOverdrive = True
        self.emitLight = True
        self.lightRadius = 50.0
        self.envEnabled |= Env.space