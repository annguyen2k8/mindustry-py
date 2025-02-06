from __future__ import annotations
from typing import *

class StatCat:
    all_stat:List[StatCat] = []
    
    general:StatCat
    power:StatCat
    liquids:StatCat
    items:StatCat
    crafting:StatCat
    function:StatCat
    optional:StatCat
    
    name:str
    id:int
    
    def __init__(self, name:str):
        self.name = name
        self.id = len(self.all_stat)
        self.all_stat.append(self)

StatCat.general = StatCat("general")
StatCat.power = StatCat("power")
StatCat.liquids = StatCat("liquids")
StatCat.items = StatCat("items")
StatCat.crafting = StatCat("crafting")
StatCat.function = StatCat("function")
StatCat.optional = StatCat("optional")