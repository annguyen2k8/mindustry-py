from enum import *

class BlockFlag(Enum):
    core:int = 1
    storage:int = 2
    generator:int = 3
    turret:int = 4
    factory:int = 5
    repair:int = 6
    battery:int = 7
    reactor:int = 8
    extinguisher:int = 9
    drill:int = 10
    shield:int = 11

    launchPad:int = 12
    unitCargoUnloadPoint:int = 13
    unitAssembler:int = 14
    hasFogRadius:int = 15

all_flags = list(BlockFlag)

all_logic_flags = [
    BlockFlag.core, BlockFlag.storage, BlockFlag.generator, BlockFlag.turret,
    BlockFlag.factory, BlockFlag.repair, BlockFlag.battery, BlockFlag.reactor,
    BlockFlag.drill, BlockFlag.shield
]