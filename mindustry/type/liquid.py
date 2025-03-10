from . import *

from mindustry.graphics import *
from mindustry.content import *

class Liquid:
    gas:bool = False
    color:Color
    gasColor:Color = Colors.lightGray
    barColor:Color
    lightColor:Color = Colors.clear
    flammability:float
    temperature:float = 0.5
    heatCapacity:float = 0.5
    viscosity:float = 0.5
    explosiveness:float
    blockReactive:bool = True
    coolant:bool = True
    moveThroughBlocks:bool = False
    incinerable:bool = True
    effect:StatusEffect = StatusEffects.none
    particleSpacing:float = 60.0
    boilPoint:float = 2.0
    capPuddles:bool = True
    hidden:bool
    canStayOn:set = set()
    def __init__(self, name:str, color:Color=Colors.black):
        self.name = name
        self.color = color

    def getContentType(self) -> ContentType:
        return ContentType.liquid