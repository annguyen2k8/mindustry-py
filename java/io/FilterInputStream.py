from .InputStream import InputStream

class FilterInputStream(InputStream):
    _in:InputStream
    def __init__(self, var1:InputStream):
        super().__init__()
        self._in = var1
    
    def read(self, var1:bytes, var2:int=None, var3:int=None) -> int:
        if var1 is None:
            return self._in.read()
        if (var2 is None and var3 is None): 
            var2 = 0; var3 = len(var)
        return self._in.read(var1, var2, var3)

    def skip(self, var1:int) -> int:
        return self._in.skip(var1)
    
    def available(self) -> int:
        return self._in.available()
    
    def close(self) -> None:
        self._in.close()
    
    def mark(self, var1:int) -> int:
        with self:
            self._in.mark(var1)
    
    def reset(self) -> None:
        with self:
            self._in.reset()
    
    def markSupported(self) -> bool:
        return self._in.markSupported()