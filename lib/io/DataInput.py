
# class DataInput:
#     def readBoolean(self) -> bool: pass
#     def readByte(self) -> bytes: pass
#     def readUnsignedByte(self) -> int: pass
#     def readShort(self) -> int: pass
#     def readUnsignedShort(self) -> int: pass
#     def readChar(self) -> str: pass
#     def readInt(self) -> int: pass
#     def readUTF(self) -> str: pass

from abc import ABC, abstractmethod
class DataInput(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def readBoolean(self) -> bool:
        pass
    @abstractmethod
    def readByte(self) -> bytes:
        pass
    @abstractmethod
    def readUnsignedByte(self) -> int: 
        pass
    @abstractmethod
    def readShort(self) -> int: 
        pass
    @abstractmethod
    def readUnsignedShort(self) -> int:
        pass
    @abstractmethod
    def readChar(self) -> str:
        pass
    @abstractmethod
    def readInt(self) -> int:
        pass
    @abstractmethod
    def readUTF(self) -> str:
        pass