from .consume import *

class ConsumeLiquidBase(Consume):
    amount:float
    def __init__(self, amount:float):
        super().__init__()
        self.amount = amount