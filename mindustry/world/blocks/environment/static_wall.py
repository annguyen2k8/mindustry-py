from mindustry.graphics import *

from .prop import Prop

class StaticWall(Prop):
    def __init__(self, name):
        super().__init__(name)
        self.breakable = True
        self.alwaysReplace = True
        self.solid = True
        self.variants = 2
        self.cacheLayer = CacheLayer.walls
        self.allowRectanglePlacement
        self.instantBuild = True
        self.ignoreBuildDarkness = True
        self.placeableLiquid = True