from . import *

class EmptyFloor(Floor):
    def __init__(self, name):
        super().__init__(name)
        self.variants = 0
        self.canShadow = False
        self.placeableOn = False
        self.solid = True