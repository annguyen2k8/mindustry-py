from mindustry.game import Schematic
from lib.io.ByteArrayInputStream import *
from lib.io.Fi import Fi

class Schematics:
    _header:bytes = b"msch"
    _version:int = 0
    
    def read(self, file:Fi) -> Schematic:
        s:Schematic = self._read(ByteArrayInputStream(file.read()))
    
    def _read(self, input_:InputStream):
        for b in self._header:
            if (input_.read() != b):
                raise Exception("Not a schematic file (missing header).")
        
        ver:int = input_.read()
        try:
            ...
        except:
            pass