from typing import *

from mindustry.graphics import *
from mindustry.world import *
from mindustry.world.meta import *

class RegenProjector(Block):
    taken:set[int] = set()
    mendMap:Dict[int, float] = {}
    
    range: int = 14
    healPercent: float = 12.0 / 60.0
    optionalMultiplier: float = 2.0
    optionalUseTime: float = 60.0 * 8.0

    # drawer:DrawBlock = DrawDefault()

    effectChance: float = 0.003
    baseColor:Color = Pal.accent
    # effect:Effect = Fx.regenParticle
    
    def __init__(self, name):
        super().__init__(name)
        self.solid = True
        self.update = True
        self.group = BlockGroup.projectors
        self.hasPower = True
        self.hasItems = True
        self.emitLight = True
        self.suppressable = True
        self.envEnabled |= Env.space
        self.rotateDraw = False