from ...block import Block
from .floor import Floor

class ShallowLiquid(Floor):
    liquidBase:Floor
    floorBase:Floor
    
    def __init__(self, name):
        super().__init__(name)
    
    def set_base(self, liquid:Block, floor:Block) -> None:
        self.liquidBase = liquid
        self.floorBase = floor
        
        self.isLiquid = True
        self.variants = self.floorBase.variants
        self.status = self.liquidBase.status
        self.liquidDrop = self.liquidBase.liquidDrop
        self.cacheLayer = self.liquidBase.cacheLayer
        self.shallow = True