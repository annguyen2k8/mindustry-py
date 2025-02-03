from ..graphics import *
from ..type import *
from ..world import *
from ..vars import *

class Blocks:
    # region environment
    
    air = AirBlock('air')
    spawn = SpawnBlock('spawn')
    removeWall = RemoveWall('remove-wall')
    removeOre = RemoveOre('remove-ore')
    cliff = Cliff('cliff')
    cliff.inEdition = False
    cliff.saveData = True
    
    # registers build blocks
    # no reference is needed here since they can be looked up by name later
    for i in range(1, Vars.maxBlockSize + 1):
        ConstructBlock(i)
    
    deepwater = Floor("deep-water")
    deepwater.speedMultiplier = 0.2
    deepwater.variants = 0
    deepwater.liquidDrop = Liquids.water
    deepwater.liquidMultiplier = 1.5
    deepwater.isLiquid = True
    # deepwater.cacheLayer = CacheLayer.water
    deepwater.status = StatusEffects.wet
    deepwater.statusDuration = 120.0
    deepwater.drownTime = 200.0
    deepwater.cacheLayer = CacheLayer.water
    deepwater.albedo = 0.9
    deepwater.supportsOverlay = True
    
    
    water = Floor("shallow-water")
    water.speedMultiplier = 0.5
    water.variants = 0
    water.status = StatusEffects.wet
    water.statusDuration = 90.0
    water.liquidDrop = Liquids.water
    water.isLiquid = True
    water.cacheLayer = CacheLayer.water
    water.albedo = 0.9
    water.supportsOverlay = True
    
    taintedWater = Floor("tainted-water")
    taintedWater.speedMultiplier = 0.5
    taintedWater.variants = 0
    taintedWater.status = StatusEffects.wet
    taintedWater.statusDuration = 90.0
    taintedWater.liquidDrop = Liquids.water
    taintedWater.isLiquid = True
    taintedWater.cacheLayer = CacheLayer.water
    taintedWater.albedo = 0.9
    taintedWater
    taintedWater.supportsOverlay = True