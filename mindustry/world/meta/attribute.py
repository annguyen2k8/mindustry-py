from __future__ import annotations
from typing import *

class Attribute:
    all_attr:List[Attribute] = []
    map_attr:Dict[str, Attribute] = {}
    
    heat:Attribute
    spores:Attribute
    water:Attribute
    oil:Attribute
    light:Attribute
    sand:Attribute
    steam:Attribute
    
    def __init__(self, id:int, name:str):
        self.id:int = id
        self.name:str = name
    
    @staticmethod
    def add(name_attr:str) -> None:
        id_attr:int = len(Attribute.all_attr) + 1
        attr:Attribute = Attribute(id_attr, name_attr)
        Attribute.all_attr.append(attr)
        Attribute.map_attr[id_attr] = attr
        return attr

Attribute.heat = Attribute.add("heat")
Attribute.spores = Attribute.add("spores")
Attribute.water = Attribute.add("water")
Attribute.oil = Attribute.add("oil")
Attribute.light = Attribute.add("light")
Attribute.sand = Attribute.add("sand")
Attribute.steam = Attribute.add("steam")