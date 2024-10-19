from __future__ import annotations
from .FilterInputStream import FilterInputStream
from .ByteArrayInputStream import InputStream
from .DataInput import DataInput
from io import BufferedReader
from typing import List, Optional

class DataInputSteam(FilterInputStream, DataInput):
    bytearr:bytearray
    chararr:List[str] = []
    readBuffer:bytearray
    lineBuffer:str = ""
    
    def __init__(self, var1: InputStream):
        self.in_ = var1
    
    def readBoolean(self) -> bool:
        var1:int = self.in_.read(1)[0]
        if (var1 < 0):
            raise Exception()
        else:
            return var1 != 0
    
    def readByte(self) -> bytes:
        var1:int = self.in_.read(1)[0]
        if (var1 < 0):
            raise Exception()
        else:
            return bytes(var1)
    
    def readUnsignedByte(self) -> int:
        var1:int = self.in_.read(1)[0]
        if (var1 < 0):
            raise Exception()
        else:
            return var1
    
    def readShort(self) -> int:
        var1:int = self.in_.read(1)[0]
        var2:int = self.in_.read(1)[0]
        if ((var1 | var2) < 0):
            raise Exception()
        else:
            return int((var1 << 8) + (var2 << 0))
    
    def readUnsignedShort(self) -> int:
        var1:int = self.in_.read(1)[0]
        var2:int = self.in_.read(1)[0]
        if ((var1 | var2) < 0):
            raise Exception()
        else:
            return (var1 << 8) + (var2 << 0)
    
    def readChar(self) -> int:
        var1:int = self.in_.read(1)[0]
        var2:int = self.in_.read(1)[0]
        if ((var1 | var2) < 0):
            raise Exception()
        else:
            return chr((var1 << 8) + (var2 << 0))
    
    def readInt(self) -> int:
        var1:int = self.in_.read(1)[0]
        var2:int = self.in_.read(1)[0]
        var3:int = self.in_.read(1)[0]
        var4:int = self.in_.read(1)[0]
        if ((var1 | var2 | var3 | var4) < 0):
            raise Exception()
        else:
            return (var1 << 24) + (var2 << 16) + (var3 << 8) + (var4 << 0)
    
    # def readLong(self, var0:Optional[DataInputSteam]) -> int:
    
    def readUTF(self) -> str:
        return self._readUTF()
    
    def _readUTF(self, var0:DataInput) -> str:
        var1:int = var0.readUnsignedShort()
        var2:object = None
        var3:object = None
        var9:bytearray
        # Line 186: char[] var10;
        var10:str
        if isinstance(var0, DataInputSteam):
            var4:DataInputSteam = var0
            if (len(var4.bytearr) < var1):
                var4.bytearr = bytes(var1 * 2)
                var4.bytearr = chr(var1 * 2)
            var9 = var4.chararr
            var10 = var4.bytearr
        else:
            var9 = bytes(var1)
            var10 = chr(var1)
        
        var7:int = 0
        var8:int = 0
        # var0.readFully(var9, 0, var1);
        
        var11:int
        while (var7 < var1):
            var11 = var9[var7] & 255
            if (var11 > 127):
                break
            var7 += 1
            var10[var8 + 1] = chr(var11)
        
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
                    var10[var8 + 1] = chr(var11)
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
                    var10[var8 + 1] = chr((var11 & 31) << 6 | var5 & 63)
                    break
                case 14:
                    var7 += 3
                    if (var7 > var1):
                        raise Exception("malformed input: partial character at end")
                    
                    var5 = var9[var7 - 2]
                    var6:bytes = var9[var7 - 1]
                    if ((var5 & 192) != 128 or (var6 & 192) != 128):
                        raise Exception("malformed input around byte " + (var7 - 1))
                    
                    var10[var8 + 1] = chr((var11 & 15) << 12 | (var5 & 63) << 6 | (var6 & 63) << 0)
                case _:
                    raise Exception("malformed input around byte " + var7)
                
        return str(var10[0:var8])