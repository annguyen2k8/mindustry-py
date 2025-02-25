from . import *

class SeaBush(Prop):
    lobes_min:int = 7
    lobes_max:int = 7
    bot_angle:float = 60.0
    origin:float = 0.1
    scl_min:float = 30.0
    scl_max:float = 50.0
    mag_min:float = 5.0
    mag_max:float = 15.0
    time_range:float = 40.0
    spread:float = 0.0
    # rand = random.Random()
    
    def __init__(self, name):
        super().__init__(name)
        self.variants = 0