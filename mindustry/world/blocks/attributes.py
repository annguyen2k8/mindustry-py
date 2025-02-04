from mindustry.world.meta import *

class Attributes:
    arr:List[float] = [0.0] * len(Attribute.all_attr)
    
    def clear(self):
        self.arr = [0.0] * len(Attribute.all_attr)
    
    def set(self, attr:Attribute, value:float) -> None:
        self.arr[attr.id] = value