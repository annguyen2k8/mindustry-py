from . import *

class HeatCrafter(GenericCrafter):
    heatRequirement:float = 10.0
    overheatScale:float = 1.0
    maxEfficiency:float = 4.0
    
    def __init__(self, name):
        super().__init__(name)