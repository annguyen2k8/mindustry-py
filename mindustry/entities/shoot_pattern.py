from __future__ import annotations
from abc import *

class ShootPattern:
    shots:int = 1
    firstShotDelay:int = 0
    shotDelay:int = 0
    
    def __init__(self):
        pass

class BulletHandler(ABC):
    def shoot(self, x:float, y:float, rotation:float, move:...=None):
        pass