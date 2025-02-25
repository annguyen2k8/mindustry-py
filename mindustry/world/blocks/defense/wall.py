from mindustry.entities import *
from mindustry.graphics import *
from mindustry.world import *
from mindustry.world.meta import *

class Wall(Block):
    lightningChance:float = -1
    lightningDamage: float = 20.0
    lightningLength: int = 17
    lightningColor: Color = Pal.surge
    # public Sound lightningSound = Sounds.spark;

    # Bullet deflection chance. -1 to disable
    chanceDeflect: float = -1.0
    flashHit: bool = False
    flashColor:Color = Colors.white
    # public Sound deflectSound = Sounds.none;
    
    def __init__(self, name):
        super().__init__(name)
        self.solid = True
        self.destructible = True
        self.group = BlockGroup.walls
        self.buildCostMultiplier = 6.0
        self.canOverdrive = False
        self.drawDisabled = False
        self.crushDamageMultiplier = 5.0
        self.priority = TargetPriority.wall

        # it's a wall of course it's supported everywhere
        self.envEnabled = Env.any