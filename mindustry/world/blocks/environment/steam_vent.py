from typing import *

from . import *

from mindustry.content import *
from mindustry.graphics import *
from mindustry.math import *
from mindustry.world import *

class SteamVent(Floor):
    offsets: List[Point2] = [
        Point2(0, 0),
        Point2(1, 0),
        Point2(1, 1),
        Point2(0, 1),
        Point2(-1, 1),
        Point2(-1, 0),
        Point2(-1, -1),
        Point2(0, -1),
        Point2(1, -1),
    ]
    
    
    effect_color:Color = Pal.vent
    effect_spacing:float = 15.0
    
    for p in offsets:
        p.sub(1, 1)
    
    def __init__(self, name):
        super().__init__(name)
        self.variants = 2
        self.parent = None