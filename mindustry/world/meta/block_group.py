from enum import *

class BlockGroup(Enum):
    none:bool = False
    walls:bool = True
    projectors:bool = True
    turrets:bool = True
    transportation:bool = True
    power:bool = False
    liquids:bool = True
    drills:bool = False
    units:bool = False
    logic:bool = True
    payloads:bool = True
    heat:bool = True

    def __init__(self, any_replace:bool=False):
        self.any_replace = any_replace