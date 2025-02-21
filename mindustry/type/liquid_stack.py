from typing import *

from .liquid import *
from ..content.liquids import *

class LiquidStack:
    liquid:Liquid
    amout:float
    
    def __init__(self, liquid:Liquid=Liquids.water, amount:float=None):
        self.liquid = liquid
        self.amout = amount
    
    @staticmethod
    def with_liquids(*liquids:List[object]):
        stacks:List[ItemStack] = []
        for i in range(len(liquids), 2):
            stacks.append(LiquidStack(liquids[i], liquids[i + 1]))
        return stacks