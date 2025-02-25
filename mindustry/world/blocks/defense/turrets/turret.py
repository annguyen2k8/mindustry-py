from . import *

from mindustry.entities import *
from mindustry.world import Block

class Turret(ReloadTurret):
    logicControlCooldown:float = 60 * 2
    timerTarget:int = Block.timers + 1
    targetInterval:float = 20.0
    maxAmmo:int = 30
    ammoPerShot:int = 1
    consumeAmmoOnce:bool = True
    heatRequirement:float = -1.0
    maxHeatEfficiency:float = 3.0
    
    inaccuracy = 0.0
    velocity_rnd = 0.0
    shoot_cone = 8.0
    shoot_x = 0.0
    shoot_y = float('-inf')
    x_rand = 0.0
    tracking_range = 0.0
    min_range = 0.0
    min_warmup = 0.0
    accurate_delay = True
    move_while_charging = True
    warmup_maintain_time = 0.0
    shoot_pattern = None 
    target_air = True
    target_ground = True
    target_blocks = True
    target_healing = False
    shoot = ShootPattern()
    controllable = True