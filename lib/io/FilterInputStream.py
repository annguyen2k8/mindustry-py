from .InputStream import InputStream
from typing import Optional

class FilterInputStream(InputStream):
    in_:InputStream
    def __init__(self, var1:InputStream):
        super().__init__()
        self.in_ = var1
    
    def read(self) -> int:
        return self.in_.read()
    
    def read(self, var1:Optional[bytearray]) -> int:
        return self.read(var1, 0, len(var1))

    def read(self, var1:Optional[bytearray], var2:int, var3:int) -> int:
        return self.in_.read(var1, var2, var3)
