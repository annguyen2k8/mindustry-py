from .content import *
from .schematic import *

import io
import zlib
import json
import struct
import pickle

class Point():
    @staticmethod
    def x(pos:int) -> int:
        return int(pos >> 16)
    
    @staticmethod
    def y(pos:int) -> int:
        return int(pos & 0xFFFF)

class DataInputStream():
    _in:io.BufferedReader
    def __init__(self, _input: io.BytesIO) -> None:
        self.buffer = io.BytesIO()
        data = _input.read()
        self.buffer.write(zlib.decompress(data))
        self.buffer.seek(0)
    
    def readShort(self) -> int:
        var1 = self.buffer.read(2)
        return struct.unpack('!h', var1)[0]
    
    def readUnsignedByte(self) -> int:
        var1 = self.buffer.read(1)
        return struct.unpack('B', var1)[0]
    
    def readUTF(self) -> str:
        # self.skipByte(1)
        # var0 = self.readUnsignedByte()
        var0 = self.readShort()
        var1 = self.buffer.read(var0)
        return var1.decode('utf-8')
    
    def readByte(self) -> bytes:
        var1 = self.buffer.read(1)
        return struct.unpack('b', var1)[0]
    
    def readInt(self) -> int:
        var1 = self.buffer.read(4)
        return struct.unpack('!i', var1)[0]
    
    def skipByte(self, i:int) -> int:
        self.buffer.read(i)

class Schematics:
    @staticmethod
    def read(_input:io.BufferedIOBase) -> Schematic:
        for b in  b"msch" :
            if (b != _input.read(1)[0]):
                raise Exception("Not a schematic file (missing header).")
        
        ver = ord(_input.read(1))
        
        stream = DataInputStream(_input)
        width, height = stream.readShort(), stream.readShort()
        if (width > 128 and height > 128):
            raise Exception("Invalid schematic: Too large (max possible size is 128x128)")
        tags:dict[str] = {}
        
        for i in range(stream.readUnsignedByte()):
            name = stream.readUTF()
            value = stream.readUTF()
            tags[name] = value
        
        blocks:dict[int, str] = {}
        length:bytes = stream.readByte()
        for i in range(length):
            name:str = stream.readUTF()
            blocks[i] = name

        total = stream.readInt()
        if (total > 128 * 128):
            raise Exception("Invalid schematic: Too many blocks.");
        
        stiles:list[Stile] = []
        for i in range(total):
            block:str = blocks.get(stream.readByte())
            position:int = stream.readInt()
            config:object = Schematics.map_config(block, stream.readByte(), position)
            rotation:bytes = stream.readByte()
            stiles.append(Stile(block, Point.x(position), Point.y(position), rotation))
        print(stiles)

    @staticmethod
    def map_config(block, value, position) -> object:
        return None