from mindustry.world.meta import *

from .mappable_content import MappableContent

class UnblockableContent(MappableContent):
    stats:Stats = Stats()
    localizedName:str
    description:str
    details:str
    ...
    
    def __init__(self, name):
        super().__init__(name)
        ...