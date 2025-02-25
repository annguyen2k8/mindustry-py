from . import *

from mindustry.world.meta import *

class AttributeCrafter(GenericCrafter):
    attribute:Attribute = Attribute.heat
    base_efficiency:float = 1.0
    boost_scale:float = 1.0
    max_boost:float = 1.0
    min_efficiency:float = -1.0
    display_efficiency_scale:float = 1.0
    display_efficiency:bool = True
    scale_liquid_consumption:bool = False
    
    def __init__(self, name):
        super().__init__(name)