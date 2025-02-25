from mindustry.graphics import *
from mindustry.ctype import *

class StatusEffect:
    name:str
    damageMultiplier:float = 1.0
    healthMultiplier:float = 1.0
    speedMultiplier:float = 1.0
    reloadMultiplier:float = 1.0
    buildSpeedMultiplier:float = 1.0
    dragMultiplier:float = 1.0
    transitionDamage:float = 0.0
    disarm:bool = False
    damage:bool
    effectChance:float = 0.15
    parentizeEffect:bool
    permanent:bool
    reactive:bool
    dynamic:bool = False
    show:bool = True
    color:Color = Colors.white
    ...
    
    def __init__(self, name:str):
        self.name = name
    
    def getContentType(self) -> ContentType:
        return ContentType.status