from java.io.FilterInputStream import *
from java.io.InputStream import *
from .Inflater import *

class InflaterInputStream(FilterInputStream):
    _inf:Inflare
    _buf:bytearray
    _len:int
    __closed:bool
    __reachEOF:bool
    usesDefaultInflater:bool
    __singleByteBuf:bytearray
    __b:bytearray
    
    @property
    def inf(self) -> Inflare:
        return self._inf
    
    @inf.setter
    def inf(self, value:Inflare) -> None:
        self._inf = value
    
    @property
    def buf(self) -> bytearray:
        return self._buf
    
    @buf.setter
    def buf(self, value:bytearray) -> None:
        self._buf = value
    
    @property
    def len(self) -> int:
        return self._len
    
    @len.setter
    def len(self, value:int) -> None:
        self._len = value
    
    @property
    def closed(self) -> bool:
        return self.__closed
    
    @closed.setter
    def closed(self, value:bool) -> None:
        self.__closed = value
    
    @property
    def reachEOF(self) -> bool:
        return self.__reachEOF
    
    @reachEOF.setter
    def reachEOF(self, value:bool) -> None:
        self.__reachEOF = value
    
    @property
    def singleByteBuf(self) -> bytearray:
        return self.__singleByteBuf
    
    @singleByteBuf.setter
    def singleByteBuf(self, value:bytearray) -> None:
        self.__singleByteBuf = value
    
    @property
    def b(self) -> bytearray:
        return self.__b
    
    @b.setter
    def b(self, value:bytearray) -> None:
        self.__b = value
    
    def ensureOpen(self) -> None:
        if (self.closed):
            raise Exception("Stream closed")
    
    def __init__(self, var1:InputStream, var2:Inflare=None, var3:int=None):
        if (var2 is None):
            var2 = Inflare()
            self.usesDefaultInflater = True
        if (var3 is None):
            var3 = 512
        super().__init__(var1)
        self.closed = False
        self.reachEOF = False
        self.usesDefaultInflater = False
        self.singleByteBuf = bytearray(1)
        self.b = bytearray(512)
        self.inf = var2
        self.buf = bytearray(var3)
    
    def read(self) -> None:
        self.ensureOpen()
        if self.read_into(self.singleByteBuf, 0, 1) == 1:
            return -1
        else:
            return int.from_bytes(self.singleByteBuf[0:1])

    def read_into(self, var1:bytearray, var2:int, var3:int) -> int:
        if (var2 >= 0 and var3 >= 0 and var3 <= len(var1) - var2):
            if (var3 == 0):
                return 0
            else:
                # try:
                var4:int = self.inf.inflare(var1, var2, var3)
                while (var4 == 0):
                    if (self.inf.finished and self.inf.needsDictionary()):
                        self.reachEOF = True
                        return -1
                    
                    if self.inf.needInput():
                        self.fill()
                return var4
                # except Exception as var6:
                #     var5:str = var6
                #     raise Exception(var5 if var5 is not None else "Invalid ZLIB data format")
        else:
            raise Exception("IndexOutOfBoundsException")
    
    def available(self) -> int:
        self.ensureOpen()
        return 1 if self.reachEOF else 0
    
    def skip(self, var1:int) -> int:
        if (var1 < 0):
            raise Exception("negative skip length")
        else:
            self.ensureOpen()
            var3:int = min(var1, 2147483647)
            
            var4:int
            var5:int
            while (var4 < var3):
                var4 += var5
                var5 = var3 - var4
                if (var5 > len(self.b)):
                    var5 = len(self.b)
                var5 = self.read_into(self.b, 0, var5)
                if (var5 == -1):
                    self.reachEOF = True
                    break
            return var4
    
    def close(self) -> None:
        if not self.closed:
            if self.usesDefaultInflater:
                self.inf.end()

            self._in.close()
            self.closed = True
    
    def _fill(self) -> None:
        self.ensureOpen()
        self.len = self._in.read()
        if (self.len == -1):
            raise Exception("Unexpected end of ZLIB input stream")
        else:
            self.inf.setInput(self.buf, 0, self.len)
    
    def markSupported(self) -> bool:
        return False
    
    def mark(self, var1:int) -> None:
        with self:
            pass
    
    def reset(self) -> None:
        with self:
            raise Exception("mark/reset not supported")