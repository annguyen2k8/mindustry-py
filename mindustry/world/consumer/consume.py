from __future__ import annotations
from typing import *

class Consume:
    optional:bool
    booster:bool
    update:bool = True
    multiplier: Callable[... ,float] = lambda b: 1.0
    
    def option(self, optional:bool, boost:bool) -> Consume:
        self.optional = optional
        self.boost = boost
        return self
    
    def boost(self) -> Consume:
        return self.option(True, True)
    
    def setUpdate(self, update:bool) -> Consume:
        self.update = update
        return self