from __future__ import annotations
from typing import *

from .content import *
from .world import *

class Schematic:
    tiles:List[Stile]
    labels:Dict[str]
    tags:Dict[str]
    width:int
    height:int
    
    def __init__(self, tiles:List[Stile], tags:Dict[str], width:int, height:int) -> None:
        self.tiles = tiles
        self.tags = tags
        self.witdh = width
        self.height = height
    
    def requirements(self):
        ...
    
    def name(self):
        return self.tags.get("name", "unknown")
    
    def description(self):
        return self.tags.get('description')

class Stile:
    block:Block
    x:int; y:int
    config:object
    rotation:bytes
    
    def __init__(self, block:Block, x:int, y:int, config:object, rotation:bytes) -> None:
        self.block = block
        self.x = x
        self.y = y
        self.config = config
        self.rotation = rotation