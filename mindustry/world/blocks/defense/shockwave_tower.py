from mindustry.graphics import *
from mindustry.world import *
from mindustry.world.meta import *

class ShockwaveTower(Block):
    range:float = 110.0
    reload:float = 60.0 * 1.5
    bulletDamage:float = 160.0
    falloffCount:float = 20.0
    shake:float = 2.0
    checkInterval:float = 8.0
    # public Sound shootSound = Sounds.bang;
    waveColor:Color = Pal.accent
    heatColor:Color = Pal.turretHeat
    shapeColor:Color = Color.valueOf("f29c83")
    cooldownMultiplier:float = 1.0
    # public Effect hitEffect = Fx.hitSquaresColor;
    # public Effect waveEffect = Fx.pointShockwave;
    shapeRotateSpeed:float = 1.0
    shapeRadius:float = 6.0
    shapeSides:int = 4
    
    def __init__(self, name):
        super().__init__(name)
        self.update = True
        self.solid = True