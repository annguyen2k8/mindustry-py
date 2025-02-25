from mindustry.graphics import *

from .liquid import Liquid

class CellLiquid(Liquid):
    colorFrom:Color = Colors.white
    colorTo:Color = Colors.white
    cell:int = 6
    spreadTarget:Liquid = None
    
    maxPread:int = 0.75
    spreadConversion:float = 1.2
    spreadDamage:float = 0.11
    removeScaling:float = 0.25
    
    def __init__(self, name, color=Colors.black):
        super().__init__(name, color)