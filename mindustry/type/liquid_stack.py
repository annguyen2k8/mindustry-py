from .liquid import *
from ..content.liquids import *

class LiquidStack:
    liquid:Liquid
    amout:float
    
    def __init__(self, liquid:Liquid=Liquids.water, amount:float=None):
        self.liquid = liquid
        self.amout = amount