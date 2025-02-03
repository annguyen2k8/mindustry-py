from ...block import *

class LaunchPad(Block):
    def __init__(self, name):
        super().__init__(name)
        self.hasItems = True
        self.solid = True
        self.update = True
        self.configurable = True
        self.flags = ...