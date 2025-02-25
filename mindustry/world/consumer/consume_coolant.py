from . import *

from mindustry.type import *

class ConsumeCoolant(ConsumeLiquidFilter):
    maxTemp:float = 0.5
    maxFlammability:float = 0.1
    allowLiquid = True
    allowGas:bool = False
    
    def __init__(self, amount:float=1.0, allowLiquid:bool=True, allowGas:bool=False):
        self.allowLiquid = allowLiquid
        self.allowGas = allowGas
        self.filter = lambda liquid: liquid.coolant and (self.allowLiquid and not liquid.gas or self.allowGas and liquid.gas) and liquid.temperature <= ConsumeCoolant.maxTemp and liquid.flammability < ConsumeCoolant.maxFlammability
        self.amount = amount