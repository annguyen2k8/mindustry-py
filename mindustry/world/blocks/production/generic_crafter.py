from typing import *

from mindustry.world.meta import *
from mindustry.type import *

from ...block import Block

class GenericCrafter(Block):
    outputItem:ItemStack = None
    outputItems:List[ItemStack] = None
    
    outputLiquid:LiquidStack = None
    outputLiquids:List[LiquidStack] = None
    
    liquidOutputDirections:List[int] = [-1]
    
    dumpExtraLiquid:bool = True
    ignoreLiquidFullness:bool = False
    
    craftTime:float = 80.0
    # public Effect craftEffect = Fx.none;
    # public Effect updateEffect = Fx.none;
    updateEffectChance:float = 0.04
    warmupSpeed:float = 0.019
    
    legacyReadWarmup:bool = False
    # public DrawBlock drawer = new DrawDefault();
    
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True
        self.hasItems = True
        # ambientSound = Sounds.machine;
        self.sync = True
        # self.ambientSoundVolume = 0.03
        self.flags.add(BlockFlag.factory)
        self.drawArrow = False