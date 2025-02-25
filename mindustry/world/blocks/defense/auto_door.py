from . import *

class AutoDoor(Wall):
    def __init__(self, name):
        super().__init__(name)
        self.solid = False
        self.solidifes = True
        self.update = True
        self.teamPassable = True
        
        self.noUpdateDisabled = True
        self.drawDisabled = True