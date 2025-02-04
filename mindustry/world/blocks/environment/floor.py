from __future__ import annotations
from typing import *

from mindustry.type import *

from mindustry.content import Blocks
from ...block import Block

class Floor(Block):
    edge:str = 'stone'
    speedMultiplier:float = 1.0
    dragMultiplier:float = 1.0
    damageTaken:float = 0.0
    drownTime:float = 0.0
    status:StatusEffect = StatusEffects.none
    statusDuration:float = 60.0
    liquidDrop:Liquid = None
    liquidMultiplier:float = 1.0
    isLiquid:bool
    overlayAlpha:float = 0.65
    supportsOverlay:bool = False
    shallow:bool = False
    blendGroup:Block
    oreDefault:bool = False
    oreScale:float = 24.0
    oreThreshold:float = 0.828
    canShadow:bool = True
    needsSurface:bool = True
    allowCorePlacement:bool = False
    wallOre:bool = False
    blendId:int = -1
    
    def __init__(self, name, variants:int=3):
        from mindustry.content.blocks import Blocks
        super().__init__(name)
        self.blendGroup = self
        self.variants = variants
        self.placeableLiquid = True
        self.allowRectanglePlacement = True
        self.instantBuild = True
        self.ignoreBuildDarkness = True
        self.wall = Blocks.air
        self.decoration = Blocks.air