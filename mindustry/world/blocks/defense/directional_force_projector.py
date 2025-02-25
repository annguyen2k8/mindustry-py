from mindustry.type import *
from mindustry.world import *
from mindustry.world.meta import *

class DirectionalForceProjector(Block):
    width:float = 30.0
    shield_health: float = 3000.0
    cooldown_normal: float = 1.75
    cooldown_liquid: float = 1.5
    cooldown_broken_base: float = 0.35
    
    # public Effect absorbEffect = Fx.absorb;
    # public Effect shieldBreakEffect = Fx.shieldBreak;
    # public @Load("@-top") TextureRegion topRegion;
    
    length: float = 40.0
    pad_size: float = 40.0
    def __init__(self, name: str):
        super().__init__(name)
        
        self.rotate = True
        self.rotate_draw = False
        
        self.update = True
        self.solid = True
        self.group = BlockGroup.projectors
        self.env_enabled |= Env.space
        # self.ambient_sound = Sounds.shield
        self.ambient_sound_volume = 0.08