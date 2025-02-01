from typing import *

from ..type import *

class Block:
    name:str
    requirements:List[ItemStack] = []
    def __init__(self, name:str):
        self.name = name