from .consume import Consume

class ConsumePower(Consume):
    usage:float
    capacity:float
    buffered:bool
    
    def __init__(self, usage:float=0.0, capacity:float=0.0, buffered:bool=False):
        super().__init__()
        self.usage = usage
        self.capacity = capacity
        self.buffered = buffered