from mindustry.graphics import *

from ...block import Block

class ShockMine(Block):
    cooldown:float = 80.0
    tileDamage: float = 5.0
    damage: float = 13.0
    length: int = 10
    tendrils: int = 6
    lightningColor = Pal.lancerLaser
    shots: int = 6
    inaccuracy: float = 0.0
    # bullet: Optional[BulletType] = None
    teamAlpha: float = 0.3
    
    def __init__(self, name):
        super().__init__(name)
        self.update = False
        self.destructible = True
        self.solid = True
        self.targetable = False