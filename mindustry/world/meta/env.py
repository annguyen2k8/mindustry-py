from enum import *

class Env(Enum):
    # is on a planet
    terrestrial:int = 1
    # is in space, no atmosphere
    space:int = 1 << 1
    # is underwater, on a planet
    underwater:int = 1 << 2
    # has spores
    spores:int = 1 << 3
    # has a scorching env effect
    scorching:int = 1 << 4
    # has oil reservoirs
    groundOil:int = 1 << 5
    # has water reservoirs
    groundWate:int = 1 << 6
    # has oxygen in the atmosphere
    oxygen:int = 1 << 7
    # all attributes combined, only used for bitmasking purposes
    other:int = 0xffffffff
    # no attributes (0)
    none:int = 0