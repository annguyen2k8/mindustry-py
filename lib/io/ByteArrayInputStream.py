from .InputStream import InputStream
from typing import Optional

class ByteArrayInputStream(InputStream):
    _buf:bytearray
    _pos:int
    _mark:int = 0
    _count:int
    
    def __init__(self, var1:bytes, var2:int=None, var3:int=None) -> None:
        super().__init__()
        if (var2 == None and var3 == None): 
            self._buf = var1
            self._pos = 0
            self._count = len(var1)
        else:
            self._buf = var1
            self._pos = var2
            self._count = min(var2 + var3, len(var1))
            self._mark = var2
    
    def read(self) -> int:
        if self._pos < self._count:
            var1 = self._buf[self._pos]
            self._pos += 1
            return var1 & 255
        else:
            return -1

    def _read(self, var1:bytes, var2:int=None, var3:int=None) -> int:
        if (var2 is None and var3 is None): 
            return self._read(var1, 0, len(var1))
        elif (var2 >= 0 and var3 >= 0 and var3 <= len(var1) - var2):
            if(self._pos >= self._count):
                return -1
            else:
                var4:int = self._count - self._pos
                if (var3 > var4):
                    var3 = var4
                if (var3 <= 0):
                    return 0
                else:
                    var1[var2:var2 + var3] = self._buf[self._pos:self._pos + var3]
                    self._pos += var3
                    return var3
        else:
            raise IndexError("IndexOutOfBoundsException")
    
    def skip(self, var1:int) -> int:
        var3:int = self._count - self._pos
        if (var1 < var3):
            var3 = 0 if var1 < 0 else var1
    
    def available(self) -> int:
        return self._count - self._pos
    
    def markSupported(self) -> bool:
        return True
    
    def mark(self, var1:int) -> int:
        self._mark = self._pos
    
    def reset(self) -> None:
        self._mark = self._mark
    
    def close(self) -> None:
        pass