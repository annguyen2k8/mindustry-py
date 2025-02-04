from .base_turret import BaseTurret

class ReloadTurret(BaseTurret):
    reloadAmor: float = 10.0
    
    def __init__(self, name):
        super().__init__(name)
        