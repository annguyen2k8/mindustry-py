from typing import *

class Consume:
    optional:bool
    booster:bool
    update:bool = True
    multiplier: Callable[... ,float] = lambda b: 1.0