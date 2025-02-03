from __future__ import annotations
from .shaders import *

class ShaderLayer:
    def __init__(self, shader:object):
        self.shader = shader

class CacheLayer:
    water = ShaderLayer(Shaders.water),
    mud = ShaderLayer(Shaders.mud),
    tar = ShaderLayer(Shaders.tar),
    slag = ShaderLayer(Shaders.slag),
    arkycite = ShaderLayer(Shaders.arkycite),
    cryofluid = ShaderLayer(Shaders.cryofluid),
    space = ShaderLayer(Shaders.space),
    normal = None
    walls = None
    
    def __init__(self):
        pass

CacheLayer.normal = CacheLayer()
CacheLayer.walls = CacheLayer()