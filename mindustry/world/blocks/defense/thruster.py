from . import *

class Thruster(Wall):
    def __init__(self, name):
        super().__init__(name)
        self.rotate = True
        self.quickRotate = True