from . import *

from mindustry import *

class MappableContent(Content):
    name:str
    def __init__(self, name:str) -> None:
        self.name = name
        Vars.content.handleMappableContent(self)
        ...