from .ZStreamRef import ZStreamRef
import threading

class InFlare:
    __zsRef:ZStreamRef
    __buf:bytearray
    __off:int
    __len:int
    __finished:bool
    __needDict:bool
    __bytesRead:int
    __byteWritten:int
    __defaultBuf:bytearray=bytearray()
    
    def __init__(self, var1:bool=None):
        if (var1 is not None):
            self.buf = self.defaultBuf
            self.zsRef = ZStreamRef(self._init(var1))
        else:
            self(False)
    
    @property
    def zsRef(self):
        return self.__zsRef
    
    @zsRef.setter
    def set_zsRef(self, value):
        self.__zsRef = value
    
    @property
    def buf(self):
        return self.__buf
    
    @buf.setter
    def set_buf(self, value):
        self.__buf = value
    
    @property
    def off(self):
        return self.__off
    
    @off.setter
    def set_off(self, value):
        self.__off = value
    
    @property
    def len(self):
        return self.__len
    
    @len.setter
    def set_len(self, value):
        self.__len = value
    
    @property
    def finished(self):
        return self.__finished
    
    @finished.setter
    def set_finished(self, value):
        self.__finished = value
    
    @property
    def needDict(self):
        return self.__needDict
    
    @needDict.setter
    def set_needDict(self, value):
        self.__needDict = value
    
    @property
    def bytesRead(self):
        return self.__bytesRead
    
    @bytesRead.setter
    def set_bytesRead(self, value):
        self.__bytesRead = value
    
    @property
    def byteWritten(self):
        return self.__byteWritten
    
    @byteWritten.setter
    def set_byteWritten(self, value):
        self.__byteWritten = value
    
    @property
    def defaultBuf(self):
        return self.__defaultBuf
    
    @defaultBuf.setter
    def set_defaultBuf(self, value):
        self.__defaultBuf = value
    
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
    
    def needInput(self) -> bool:
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
                var6:int =self.inflareByte(self.zsRef.address, var1, var2, var3)
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
    def _initID(self) -> None:
        pass
    
    @staticmethod
    def _init(self, var0:bool):
        pass
    
    @staticmethod
    def setDictionary(self, var0:int, var2:bytes, var3:int, var4:int) -> None:
        pass
    
    @staticmethod
    def inflateBytes(self, var0:int, var2:bytes, var3:int, var4:int) -> None:
        pass
    
    @staticmethod
    def _getAdler(self, var1:int) -> int:
        pass
    
    @staticmethod
    def _reset(self, var0:int) -> None:
        pass
    
    @staticmethod
    def _end(self, var0:int) -> None:
        pass