from .InputStream import InputStream
from typing import Optional

class ByteArrayInputStream(InputStream):
    _buf:bytearray
    _pos:int
    _mark:int = 0
    _count:int
    
    @property
    def buf(self) -> bytearray:
        return self._buf
    
    @buf.setter
    def buf(self, value:bytearray) -> None:
        self._buf = value
    
    @property
    def pos(self) -> int:
        return self._pos
    
    @pos.setter
    def pos(self, value:int) -> None:
        self._pos = value
    
    @property
    def count(self) -> int:
        return self._count
    
    @count.setter
    def count(self, value:int) -> None:
        self._count = value
    
    def __init__(self, var1:bytes, var2:int=None, var3:int=None) -> None:
        super().__init__()
        if (var2 == None and var3 == None): 
            self.buf = var1
            self.pos = 0
            self._count = len(var1)
        else:
            self.buf = var1
            self.pos = var2
            self.count = min(var2 + var3, len(var1))
            self._mark = var2
    
    def read(self) -> int:
        if self._pos < self._count:
            var1 = self._buf[self._pos]
            self._pos += 1
            return var1 & 255
        else:
            return -1

    def read_into(self, var1:bytes, var2:int, var3:int) -> int:
        if (var2 >= 0 and var3 >= 0 and var3 <= len(var1) - var2):
            if(self.pos >= self.count):
                return -1
            else:
                var4:int = self.count - self.pos
                if (var3 > var4):
                    var3 = var4
                if (var3 <= 0):
                    return 0
                else:
                    var1[var2:var2 + var3] = self.buf[self.pos:self.pos + var3]
                    self.pos += var3
                    return var3
        else:
            raise IndexError("IndexOutOfBoundsException")
    
    def skip(self, var1:int) -> int:
        var3:int = self.count - self.pos
        if (var1 < var3):
            var3 = 0 if var1 < 0 else var1
        return var3
    
    def available(self) -> int:
        with self:
            return self.count - self.pos
    
    def markSupported(self) -> bool:
        return True
    
    def mark(self, var1:int) -> int:
        self._mark = self.pos
    
    def reset(self) -> None:
        self.pos = self._mark
    
    def close(self) -> None:
        pass