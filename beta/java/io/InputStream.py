from abc import ABC
from abc import abstractmethod
import threading

class InputStream(ABC):
    __MAX_SKIP_BUFFER_SIZE:int = 2048
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
    
    def read(self) -> int:
        pass
    
    def read_bytes(self, var1:bytearray) -> int:
        return self.read_into(var1, 0, len(var1))
    
    def read_into(self, var1:bytes, var2:int, var3:int) -> int:
        if (var2 >= 0 and var3 >= 0 and var3 <= len(var1) - var2):
            if (var3 == 0):
                return 0
            else:
                var4:int = self.read()
                if (var4 == -1):
                    return -1
                else:
                    var1[var2] = bytes(var4)
                    var5:int = 1
                    try:
                        while (var5 < var3):
                            var4 = self.read()
                            if (var4 == -1):
                                break
                            var1[var2 + var5] = bytes(var4)
                    except Exception:
                        pass
                    return var5
        else:
            raise Exception("IndexOutOfBoundsException")
    
    def skip(self, var1:int) -> int:
        var3:int = var1
        if (var3 < 0):
            return 0
        else:
            var6:int = int(min(2048, var1))
            var5:int
            var7 = bytearray(var6)
            while var3 > 0:
                var5 = self.read_into(var7, 0, min(var6, var3))
                if var5 < 0:
                    break
                var3 -= var5
            return var1 - var3
    
    def available(self) -> int:
        return 0
    
    def close(self) -> None:
        pass
    
    def markSupported(self) -> bool:
        return False
    
    def mark(self, var1:int) -> None:
        with self:
            pass
    
    def reset(self):
        with self:
            raise Exception("mark/reset not supported") 
    
    def markSupported(self) -> bool:
        return False
    
    def __enter__(self):
        self.lock.acquire()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()