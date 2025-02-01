from __future__ import annotations
from .FilterInputStream import FilterInputStream
from .ByteArrayInputStream import InputStream
from .DataInput import DataInput
from io import BufferedReader

class DataInputSteam(FilterInputStream, DataInput):
    bytearr:bytearray = bytearray(80)
    chararr:list[str] = ['']*80
    readBuffer:bytearray = bytearray(8)
    lineBuffer:list[str] = []
    
    def __init__(self, var1: InputStream):
        super().__init__(var1)
    
    def read(self, var1:bytearray) -> int:
        return self._in.read_into(var1, 0, len(var1))
    
    
    def read_into(self, var1:bytearray, var2:int=None, var3:int=None) -> int:
        return self._in.read_into(var1, var2, var3)
    
    def readFully(self, var1:bytearray, var2:int, var3:int) -> int:
        if (var2 is None and var3 is None):
            var2 = 0; var3 = len(var3)
        if (var3 < 0):
            raise Exception("IndexOutOfBoundsException")
        else:
            var5:int
            var4:int = 0
            while (var4 < var3):
                var4 += var5
                var5 = self._in.read(var1, var2 + var4, var3 - var4)
                if (var5 < 0):
                    raise Exception("EOFException")
    
    def skipBytes(self, var1:int) -> int:
        var2:int = 0
        while var2 < var1:
            var3 = int(self._in.skip(var1 - var2))
            if var3 <= 0:
                break
            var2 += var3
        return var2
    
    def readBoolean(self) -> bool:
        var1:int = self._in.read()
        if (var1 < 0):
            raise Exception()
        else:
            return var1 != 0
    
    def readByte(self) -> bytes:
        var1:int = self._in.read()
        if (var1 < 0):
            raise Exception()
        else:
            return bytes(var1)
    
    def readUnsignedByte(self) -> int:
        var1:int = self._in.read()
        if (var1 < 0):
            raise Exception()
        else:
            return var1
    
    def readShort(self) -> int:
        var1:int = self._in.read()
        var2:int = self._in.read()
        if ((var1 | var2) < 0):
            raise Exception()
        else:
            return int((var1 << 8) + (var2 << 0))
    
    # function readUnsignedShort same as function readShort
    # idk why?
    
    def readUnsignedShort(self) -> int:
        var1:int = self._in.read()  
        var2:int = self._in.read()
        if ((var1 | var2) < 0):
            raise Exception()
        else:
            return (var1 << 8) + (var2 << 0)
    
    def readChar(self) -> int:
        var1:int = self._in.read()
        var2:int = self._in.read()
        if ((var1 | var2) < 0):
            raise Exception()
        else:
            return chr((var1 << 8) + (var2 << 0))
    
    def readInt(self) -> int:
        var1:int = self._in.read()
        var2:int = self._in.read()
        var3:int = self._in.read()
        var4:int = self._in.read()
        if ((var1 | var2 | var3 | var4) < 0):
            raise Exception()
        else:
            return (var1 << 24) + (var2 << 16) + (var3 << 8) + (var4 << 0)
    
    def readLong(self) -> int:
        self.readFully(self.readBuffer, 0, 8)
        return (self.readBuffer[0] << 56 + (self.readBuffer[1] & 255) << 48 + (self.readBuffer[2] & 255) << 40 + (self.readBuffer[3] & 255) << 32 + (self.readBuffer[4] & 255) << 24 + (self.readBuffer[5] & 255) << 16 + (self.readBuffer[6] & 255) << 8  + (self.readBuffer[7] & 255))

    def readFloat(self) -> float:
        import struct
        int_bits = self.readInt()
        return struct.unpack('!f', struct.pack('!I', int_bits))[0]

    def readDouble(self) -> float:
        import struct
        long_bits = self.readLong()
        return struct.unpack('!d', struct.pack('!Q', long_bits))[0]
    
    def read_line(self) -> str:
        if self.lineBuffer is None:
            self.lineBuffer = [''] * 128

        var1 = self.lineBuffer
        var2 = len(var1)
        var3 = 0

        while True:
            var4 = self._in.read()
            match var4:
                case 13:
                    var5 = self._in.read()
                    if (var5 != 10 and var5 != -1):
                        # if (!(this.in instanceof PushbackInputStream)) {
                        #     this.in = new PushbackInputStream(this.in);
                        # }

                        # ((PushbackInputStream)this.in).unread(var5);
                        ...
                case -1:
                    pass
                case 10:
                    if (var4 == -1 and var3 == 0):
                        return None
                    return ''.join(var1[:var3])
            
            var2 -= 1
            if (var2 < 0):
                var1 = [''] * (var3 + 128)
                var2 = len(var1 - var3 - 1)
                var1[0:var3] = self.lineBuffer[0:var3]
                self.lineBuffer = var1
            
            var1[var3] = chr(var4)
            var3 += 1

    def readUTF(self, var0:DataInput=None) -> str:
        if var0 is None:
            var0 = self
        var1:int = var0.readUnsignedShort()
        var2:object = None
        var3:object = None
        var9:bytearray
        var10:list[str]
        if isinstance(var0, DataInputSteam):
            var4:DataInputSteam = var0
            if (len(var4.bytearr) < var1):
                var4.bytearr = bytes(var1 * 2)
                var4.bytearr = chr(var1 * 2)
            var9 = var4.chararr
            var10 = var4.bytearr
        else:
            var9 = bytearray(var1)
            var10 = [''] * var1
        
        var7:int = 0
        var8:int = 0
        var0.readFully(var9, 0, var1);
        
        var11:int
        while (var7 < var1):
            var11 = var9[var7] & 255
            if (var11 > 127):
                break
            var7 += 1
            var10[var8] = chr(var11)
            var8 += 1
        
        while (var7 < var1):
            var11 = var9[var7] & 255
            var5:bytes
            match (var11 >> 4):
                case 0: pass
                case 1: pass
                case 2: pass
                case 3: pass
                case 4: pass
                case 5: pass
                case 6: pass
                case 7:
                    var7 += 1
                    var10[var8] = chr(var11)
                    var8 += 1
                    break
                case 8: pass
                case 9: pass
                case 10: pass
                case 11: pass
                case 12: pass
                case 13:
                    var7 += 2
                    if (var7 > var1):
                        raise Exception("malformed input: partial character at end")
                    var5 = var9[var7 - 1]
                    if ((var5 & 192) != 128):
                        raise Exception("malformed input around byte " + var7)
                    var10[var8] = chr((var11 & 31) << 6 | var5 & 63)
                    var8 += 1
                    break
                case 14:
                    var7 += 3
                    if (var7 > var1):
                        raise Exception("malformed input: partial character at end")
                    
                    var5 = var9[var7 - 2]
                    var6:bytes = var9[var7 - 1]
                    if ((var5 & 192) != 128 or (var6 & 192) != 128):
                        raise Exception("malformed input around byte " + (var7 - 1))
                    
                    var10[var8] = chr((var11 & 15) << 12 | (var5 & 63) << 6 | (var6 & 63) << 0)
                    var8 += 1
                case _:
                    raise Exception("malformed input around byte " + var7)
                
        return str(var10[0:var8])