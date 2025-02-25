from mindustry.world.meta import *
from mindustry.graphics import *
from mindustry.type import *

from .base_turret import BaseTurret

class BuildTurret(BaseTurret):
    targetInterval:int = 15
    buildSpeed:float = 1.0
    buildBeamOffset:float = 5.0
    unitType:UnitType = None
    elevation:float = -1.0
    heatColor:Color = Pal.accent.cpy().set_a(0.9);
    
    def __init__(self, name):
        super().__init__(name)
        self.group = BlockGroup.turret
        self.sync = False
        self.rotateSpeed = 10.0
        self.suppressable = True