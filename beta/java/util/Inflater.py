from .ZStreamRef import ZStreamRef
import threading

class Inflare:
    __zsRef:ZStreamRef
    __buf:bytearray = bytearray()
    __off:int = 0
    __len:int = 0
    __finished:bool = None
    __needDict:bool = None
    __bytesRead:int = 0
    __byteWritten:int = 0
    __defaultBuf:bytearray=bytearray(0)
    
    @property
    def zsRef(self) -> ZStreamRef:
        return self.__zsRef
    
    @zsRef.setter
    def zsRef(self, value:ZStreamRef):
        self.__zsRef = value
    
    @property
    def buf(self) -> bytearray:
        return self.__buf
    
    @buf.setter
    def buf(self, value:bytearray):
        self.__buf = value
    
    @property
    def off(self) -> int:
        return self.__off
    
    @off.setter
    def off(self, value:int):
        self.__off = value
    
    @property
    def len(self) -> int:
        return self.__len
    
    @len.setter
    def len(self, value:int):
        self.__len = value
    
    @property
    def finished(self) -> bool:
        return self.__finished
    
    @finished.setter
    def finished(self, value:bool):
        self.__finished = value
    
    @property
    def needDict(self) -> bool:
        return self.__needDict
    
    @needDict.setter
    def needDict(self, value:bool):
        self.__needDict = value
    
    @property
    def bytesRead(self) -> int:
        return self.__bytesRead
    
    @bytesRead.setter
    def bytesRead(self, value:int):
        self.__bytesRead = value
    
    @property
    def byteWritten(self) -> int:
        return self.__byteWritten
    
    @byteWritten.setter
    def byteWritten(self, value:int):
        self.__byteWritten = value
    
    @property
    def defaultBuf(self) -> bytearray:
        return self.__defaultBuf
    
    def __init__(self, var1:bool=None):
        if (var1 is not None):
            self.buf = self.defaultBuf
            self.zsRef = ZStreamRef(self._init(var1))
        else:
            self.__init__(False)
    
    def setInput(self, var1:bytes, var2:int=None, var3:int=None) -> None:
        if (var2 is None and var3 is None): 
            return self.setInput(var1, 0, len(var1))
        elif (var2 >= 0 and var3 >= 0 and var2 <= len(var1) - var3):
            with self.zsRef:
                self.buf = var1
                self.off = var2
                self.len = var3
        else:
            raise ValueError("ArrayIndexOutOfBoundsException")
    
    def setDictionary(self, var1:bytes, var2:int=None, var3:int=None) -> None:
        if (var2 is None and var3 is None): 
            return self.setDictionary(var1, 0, len(var1))
        elif (var2 >= 0 and var3 >= 0 and var2 <= len(var1) - var3):
            with self.zsRef:
                self.__ensureOpen()
                self.setDictionary(self.zsRef.address, var1, var2, var3)
                self.needDict = False
        else:
            raise ValueError("ArrayIndexOutOfBoundsException")
    
    def getRemaining(self) -> int:
        with self.zsRef:
            return self.len
    
    def needsInput(self) -> bool:
        with self.zsRef:
            return self.__len <= 0
    
    def needsDictionary(self) -> bool:
        with self.zsRef:
            return self.needDict
    
    def inflare(self, var1:bytes, var2:int=None, var3:int=None) -> int:
        if (var2 is None and var3 is None): 
            return self.inflare(var1, 0, len(var1))
        elif (var2 >= 0 and var3 >= 0 and var2 <= len(var1) - var3):
            with self.zsRef:
                self.__ensureOpen()
                var5:int = self.len
                var6:int = self.inflateBytes(self.zsRef.address, var1, var2, var3)
                self.byteWritten += var6
                self.bytesRead += var5 - self.len
        else:
            raise ValueError("ArrayIndexOutOfBoundsException")
    
    def getAdler(self) -> int:
        with self.zsRef:
            self.__ensureOpen()
            return self._getAdler(self.zsRef.address)
    
    def getTotalIn(self) -> int:
        return self.getBytesRead()
    
    def getBytesRead(self) -> int:
        with self.zsRef:
            self.__ensureOpen()
            return self.bytesRead
    
    def getTotalOut(self) -> int:
        return self.getBytesWritten()
    
    def getBytesWritten(self) -> int:
        with self.zsRef:
            self.__ensureOpen()
            return self.byteWritten
    
    def reset(self) -> None:
        with self.zsRef:
            self.__ensureOpen()
            self.zsRef.clear()
            self.buf = self.defaultBuf
            self.finished = False
            self.off = self.len = 0
            self.bytesRead = self.byteWritten = 0
    
    def end(self) -> None:
        with self.zsRef:
            var2 = self.zsRef.address
            self.zsRef.clear()
            if (var2 == 0):
                self.end(var2)
                self.buf = None
    
    def _finalize(self) -> None:
        self.end()
    
    def __ensureOpen(self) -> None:
        if not self.zsRef.lock.locked():
            raise AssertionError("Thread does not hold the lock")
        elif (self.zsRef.address == 0):
            raise ValueError("NullPointerException(\"Inflater has been closed\")")
    
    def ended(self) -> bool:
        with self.zsRef:
            return self.zsRef.address == 0    
    
    @staticmethod
    def _initID() -> None:
        pass
    
    @staticmethod
    def _init(var0:bool) -> bool:
        pass
    
    @staticmethod
    def setDictionary(var0:int, var2:bytes, var3:int, var4:int) -> None:
        pass
    
    def inflateBytes(self, var0:int, var2:bytes, var3:int, var4:int) -> None:
        return 0
    
    @staticmethod
    def _getAdler(var1:int) -> int:
        pass
    
    @staticmethod
    def _reset(var0:int) -> None:
        pass
    
    @staticmethod
    def _end(var0:int) -> None:
        pass