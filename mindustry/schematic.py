from __future__ import annotations
from beta.content import *

class Schematic:
    tiles:list[Stile]
    labels:list
    tags:dict[str]
    width:int; height:int
    
    def __init__(self, tiles:list[Stile], tags:dict[str], width:int, height:int) -> None:
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
    
    def set(self, other: Stile) -> None:
        self.block = other.block
        self.x = other.x
        self.y = other.y
        self.config = other.config
        self.rotation = other.rotation
        return self
    
    def copy(self) -> None:
        return Stile(self.block, self.x, self.y, self.config, self.rotation)
    
    def __repr__(self) -> str:
        pass