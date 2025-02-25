from mindustry.world import *
from mindustry.world.meta import *
from mindustry.world.consumer import *


class ForceProjector(Block):
    phaseUseTime:float = 350.0

    phaseRadiusBoost:float = 80.0
    phaseShieldBoost:float = 400.0
    radius:float = 101.7
    sides:int  = 6
    shieldRotation:float  = 0.0
    shieldHealth:float = 700
    cooldownNormal:float = 1.75
    cooldownLiquid:float = 1.5
    cooldownBrokenBase:float = 0.35
    coolantConsumption:float = 0.1
    consumeCoolant:bool = True
    crashDamageMultiplier:float = 2.0
    
    itemConsumer:Consume
    coolantConsumer:Consume
    
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True
        self.group = BlockGroup.projectors
        self.hasPower = True
        self.hasLiquids = True
        self.hasItems = True
        self.envEnabled |= Env.space
        # ambientSound = Sounds.shield;
        # ambientSoundVolume = 0.08f;
        self.flags = set(BlockFlag.shield)
        
        if self.consumeCoolant:
            self.coolantConsumer = ConsumeCoolant(self.coolantConsumption).boost().update(False)
            self.consume(self.coolantConsumer)