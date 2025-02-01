from beta.game import Schematic
from java.io.ByteArrayInputStream import *
from java.io.DataInputStream import *
from java.io.Fi import Fi
from java.util.InflaterInputStream import *

class Schematics:
    _header:bytes = b"msch"
    _version:int = 0
    
    def read(self, file:Fi) -> Schematic:
        s:Schematic = self._read(ByteArrayInputStream(file.read()))
    
    def _read(self, input_:ByteArrayInputStream):
        for b in self._header:
            if (input_.read() != b):
                raise Exception("Not a schematic file (missing header).")
        ver:int = input_.read()
        stream = DataInputSteam(InflaterInputStream(input_))
        print(type(input_))
        print(stream.readShort()) 