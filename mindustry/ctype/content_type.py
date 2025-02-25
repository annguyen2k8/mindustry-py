from __future__ import annotations
from typing import *
from enum import Enum

from mindustry.type import *
from mindustry.world import *

class ContentType(Enum):
    item:ContentType
    block:ContentType
    mech_UNUSED:ContentType
    bullet:ContentType
    liquid:ContentType
    status:ContentType
    unit:ContentType
    weather:ContentType
    effect_UNUSED:ContentType
    sector:ContentType
    loadout_UNUSED:ContentType
    typeid_UNUSED:ContentType
    error:ContentType
    planet:ContentType
    ammo_UNUSED:ContentType
    team:ContentType
    unitCommand:ContentType
    unitStance:ContentType
    
    def __init__(self, contentClass):
        self.contentClass = contentClass

ContentType.item = ContentType(Item.__class__)
ContentType.block = ContentType(Block.__class__)