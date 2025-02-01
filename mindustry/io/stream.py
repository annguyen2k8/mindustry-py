import io
import zlib
import struct

class Stream():
    _in:io.BufferedReader
    def __init__(self, _input: io.BytesIO) -> None:
        self.buffer = io.BytesIO()
        data = _input.read()
        self.buffer.write(zlib.decompress(data))
        self.buffer.seek(0)
    
    def readShort(self) -> int:
        var1 = self.buffer.read(2)
        return struct.unpack('!h', var1)[0]
    
    def readUnsignedShort(self) -> int:
        var1 = self.buffer.read(2)
        return struct.unpack('!H', var1)[0]
    
    def readUnsignedByte(self) -> int:
        var1 = self.buffer.read(1)
        return struct.unpack('!B', var1)[0]
    
    def readUTF(self) -> str:
        var0 = self.readUnsignedShort()
        var1 = self.buffer.read(var0)
        return var1.decode('utf-8')
    
    def readByte(self) -> bytes:
        var1 = self.buffer.read(1)
        return struct.unpack('b', var1)[0]
    
    def readInt(self) -> int:
        var1 = self.buffer.read(4)
        return struct.unpack('!i', var1)[0]
    
    def readLong(self) -> int:
        var1 = self.buffer.read(4)
        return struct.unpack('<q', var1)[0] 
    
    def readFloat(self) -> float:
        var1 = self.buffer.read(4)
        return struct.unpack('<f', var1)[0]
    
    def readBool(self) -> bool:
        var1 = self.buffer.read(1)
        return struct.unpack('?', var1)[0]
    
    def readDouble(self) -> float:
        var1 = self.buffer.read(8)
        return struct.unpack('<d', var1)[0]