from mindustry.world.meta import *
from mindustry.entities import *

from ....block import Block

class BaseTurret(Block):
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True
        self.outlineIcon = True
        self.attacks = True
        self.priority = TargetPriority.turret
        self.group = BlockGroup.turrets
        self.flags = set().add(BlockFlag.turret)
